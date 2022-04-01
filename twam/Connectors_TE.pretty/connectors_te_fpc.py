#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

contact_types = ["TOP CONTACT", "BOTTOM CONTACT"]

number_of_positions_values = [val for val in range(5,51)]

pad_size_x = 0.3
pad_size_y = 1.1
mounting_pad_size_x = 2.3
mounting_pad_size_y = 3.1

pad_pitch = 0.5

mounting_pad_offset_x_left = 2.82
mounting_pad_offset_y_top = 0.7

def C(number_of_positions):
	return (number_of_positions-1)*pad_pitch

def A(number_of_positions):
	return (number_of_positions-1)*pad_pitch+5.93

case_offset_y = 0.7
case_size_y = 4.4

line_width = 0.15
crtyd_width = 0.05
crtyd_spacing = 0.5

middle_partnum = {
	"TOP CONTACT": 1734839,
	"BOTTOM CONTACT": 1734592
}

def crtyd_round(value, direction):
	if direction > 0:
		return math.ceil(value/0.05)*0.05
	else:
		return math.floor(value/0.05)*0.05

def name(number_of_positions, contact_type):
	positions_string = "%02u" % number_of_positions
	return "%c-%u-%c" % (positions_string[0], middle_partnum[contact_type], positions_string[1])

def description(number_of_positions, contact_type):
	return "TE Connectivity FPC Connector, %.1fmm PITCH, %s, SMT TYPE" % (pad_pitch, contact_type)

def tags(number_of_positions, contact_type):
	return "TE Connectivity %02ux%02u %s smd %.1f mm pitch fpc headers" % (
		1,
		number_of_positions,
		contact_type.lower(),
		pad_pitch)

def pad(position, x, y, diameter_pad_x, diameter_pad_y):
	return "  (pad %s smd rect (at %.3f %.3f) (size %.3f %.3f) (layers F.Cu F.Paste F.Mask))\n" % (position, x, y, diameter_pad_x, diameter_pad_y)

for contact_type in contact_types:
	for number_of_positions in number_of_positions_values:
		filename = "%s.kicad_mod" % (name(number_of_positions, contact_type))

		x_origin = 0
#		y_origin = - (-pad_size_y/2.0 + (mounting_pad_offset_y_top + mounting_pad_size_y)/2.0)
		y_origin = - (-pad_size_y/2.0 + mounting_pad_offset_y_top + mounting_pad_size_y/2.0) /2.0

		x_start = -C(number_of_positions)/2.0
		x_end = C(number_of_positions)/2.0
		x_mid = (x_start+x_end)/2.0

		y_start = 0

		output = open(filename, 'w')

		output.write("(module %s (layer F.Cu) (tedit %X)\n" % (name(number_of_positions, contact_type), int(time.time())))
		output.write("  (attr smd)\n")

		# description
		output.write("  (descr \"%s\")\n" % (description(number_of_positions, contact_type)))

		# tags
		output.write("  (tags \"%s\")\n" % (tags(number_of_positions, contact_type)))

		# reference
		output.write("  (fp_text reference REF** (at %.3f %.3f 270) (layer F.SilkS)\n" % (x_start - mounting_pad_offset_x_left - 1, y_start))
		output.write("    (effects (font (size 1 1) (thickness 0.15)))\n")
		output.write("  )\n")

		#value
		output.write("  (fp_text value %s (at %.3f %.3f 270) (layer F.Fab)\n" % (name(number_of_positions, contact_type), x_end + mounting_pad_offset_x_left + 1, y_start))
		output.write("    (effects (font (size 1 1) (thickness 0.15)))\n")
		output.write("  )\n")

 		# pads
		for pos in range(1, number_of_positions+1):
			output.write(pad(pos if contact_type == "BOTTOM CONTACT" else number_of_positions+1-pos , x_origin+x_start+(pos-1)*pad_pitch, y_origin+y_start, pad_size_x, pad_size_y))

		#mounting pads
		for pos in ["F1","F2"]:
			x = x_origin + x_start - mounting_pad_offset_x_left + mounting_pad_size_x/2.0
			y = y_origin + y_start - pad_size_y/2.0 + mounting_pad_offset_y_top + mounting_pad_size_y/2.0
			if pos == "F2":
				x *= -1
			output.write(pad(pos, x, y, mounting_pad_size_x, mounting_pad_size_y))


		x_lines = [
			x_origin - A(number_of_positions)/2.0,
			x_origin + A(number_of_positions)/2.0]
		y_lines = [
			y_origin + y_start - pad_size_y/2.0 + case_offset_y,
			y_origin + y_start - pad_size_y/2.0 + mounting_pad_offset_y_top + mounting_pad_size_y,
			y_origin + y_start - pad_size_y/2.0 + case_offset_y + case_size_y]

		# drawing
		for y in [y_lines[-1]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
				x_lines[0],
				y,
				x_lines[-1],
				y,
				line_width
				))

		for x in x_lines:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
				x,
				y_lines[1],
				x,
				y_lines[-1],
				line_width
				))

		# # hole
		# if (termination_type == "RA"):
		# 	for x in [x_mid-hole_width/2.0, x_mid+hole_width/2.0]:
		# 		output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
		# 			x,
		# 			y_lines[0]+hole_depth,
		# 			x,
		# 			y_lines[0],
		# 			line_width
		# 			))

		# 	output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
		# 		x_mid-hole_width/2.0,
		# 		y_lines[0]+hole_depth,
		# 		x_mid+hole_width/2.0,
		# 		y_lines[0]+hole_depth,
		# 		line_width
		# 		))

		# # pin indicator
		# if (termination_type == "RA"):
		# 	pin_indicator_offset = 1.0 if number_of_positions <= 3 else 0.0
		# 	output.write("  (fp_poly (pts (xy %.3f %.3f) (xy %.3f %.3f) (xy %.3f %.3f)) (layer F.SilkS) (width %.3f))\n" % (
		# 		-pin_indicator_offset,
		# 		y_lines[0]+pin_indicator_distance_to_top+pin_indicator_size,
		# 		-pin_indicator_offset-pin_indicator_size/2.0,
		# 		y_lines[0]+pin_indicator_distance_to_top,
		# 		-pin_indicator_offset+pin_indicator_size/2.0,
		# 		y_lines[0]+pin_indicator_distance_to_top,
		# 		line_width
		# 		))

		# if (termination_type == "RA"):
		# 	# pin drawings
		# 	for pos in xrange(1, number_of_positions+1):
		# 		x = (pos-1)*pin_pitch
		# 		output.write("  (fp_poly (pts (xy %.3f %.3f) (xy %.3f %.3f) (xy %.3f %.3f) (xy %.3f %.3f)) (layer F.SilkS) (width %.3f))\n" % (
		# 			x+pin_diameter/2.0,
		# 			-Rx_pin_to_plastic,
		# 			x-pin_diameter/2.0,
		# 			-Rx_pin_to_plastic,
		# 			x-pin_diameter/2.0,
		# 			-(pin_pitch+pad_diameter/2.0),
		# 			x+pin_diameter/2.0,
		# 			-(pin_pitch+pad_diameter/2.0),
		# 			line_width
		# 			))

			# for pos in xrange(int(number_of_positions/2.0), int(number_of_positions/2.0)+2):
			# 	x = (pos-1)*pin_pitch
			# 	output.write("  (fp_poly (pts (xy %.3f %.3f) (xy %.3f %.3f) (xy %.3f %.3f) (xy %.3f %.3f)) (layer F.SilkS) (width %.3f))\n" % (
			# 		x+pin_diameter/2.0,
			# 		y_lines[0]+hole_depth-pin_length_in_hole,
			# 		x-pin_diameter/2.0,
			# 		y_lines[0]+hole_depth-pin_length_in_hole,
			# 		x-pin_diameter/2.0,
			# 		y_lines[0]+hole_depth,
			# 		x+pin_diameter/2.0,
			# 		y_lines[0]+hole_depth,
			# 		line_width
			# 		))

		# courtyard
		crtyd_x_lines = [
			crtyd_round(x_origin + x_start - mounting_pad_offset_x_left - crtyd_spacing, -1),
			crtyd_round(x_origin + x_start - pad_size_x/2.0 - crtyd_spacing, -1),
			crtyd_round(x_origin + x_end + pad_size_x/2.0 + crtyd_spacing, 1),
			crtyd_round(x_origin + x_end + mounting_pad_offset_x_left + crtyd_spacing, 1)]
		crtyd_y_lines = [
			crtyd_round(y_origin + y_start - pad_size_y/2.0 - crtyd_spacing, -1),
			crtyd_round(y_origin + y_start - pad_size_y/2.0 + mounting_pad_offset_y_top - crtyd_spacing, -1),
			crtyd_round(y_origin + y_start - pad_size_y/2.0 + case_offset_y + case_size_y + crtyd_spacing, 1)]

		# top line
		for y in [crtyd_y_lines[0]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				crtyd_x_lines[1],
				y,
				crtyd_x_lines[-2],
				y,
				crtyd_width
				))

		# middle line
		for y in [crtyd_y_lines[1]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				crtyd_x_lines[0],
				y,
				crtyd_x_lines[1],
				y,
				crtyd_width
				))
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				crtyd_x_lines[-2],
				y,
				crtyd_x_lines[-1],
				y,
				crtyd_width
				))

		# bottom line
		for y in [crtyd_y_lines[-1]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				crtyd_x_lines[0],
				y,
				crtyd_x_lines[-1],
				y,
				crtyd_width
				))

		# top part
		for x in [crtyd_x_lines[1], crtyd_x_lines[-2]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				x,
				crtyd_y_lines[0],
				x,
				crtyd_y_lines[1],
				crtyd_width
				))

		# bottom part
		for x in [crtyd_x_lines[0], crtyd_x_lines[-1]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				x,
				crtyd_y_lines[-2],
				x,
				crtyd_y_lines[-1],
				crtyd_width
				))

		# pcb edge line
		pcb_edge_y = y_origin + y_start - pad_size_y/2.0+ mounting_pad_offset_y_top + mounting_pad_size_y + 0.6
		output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.Fab) (width %.3f))\n" % (
			crtyd_x_lines[0],
			pcb_edge_y,
			crtyd_x_lines[-1],
			pcb_edge_y,
			crtyd_width
			))

		output.write(")\n")
		output.close()
