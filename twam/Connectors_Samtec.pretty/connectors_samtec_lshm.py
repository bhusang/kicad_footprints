#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math

#http://suddendocs.samtec.com/prints/lshm-1xx-xx.x-xx-dv-a-x-x-tr-mkt.pdf
#http://suddendocs.samtec.com/prints/lshm-1xx-xx.x-x-dv-a-x-x-tr-footprint.pdf

contact_types = ["TOP CONTACT", "BOTTOM CONTACT"]

number_of_positions_values = [5,10,20,30,40,50]
number_of_rows = 2

pad_size_x = 0.3
pad_size_y = 1.5

pad_pitch_x = 0.5
pad_pitch_y = 3.7

def A(number_of_positions):
	return (number_of_positions-1)*pad_pitch_x

def B(number_of_positions):
	return (number_of_positions-1)*pad_pitch_x + 2.5

def C(number_of_positions):
	return (number_of_positions-1)*pad_pitch_x + 5.45

def D(number_of_positions):
	return (number_of_positions-1)*pad_pitch_x + 6.75

def E(number_of_positions):
	return (number_of_positions-1)*pad_pitch_x + 5.2

npth_drill_size = 1.45
pth_drill_size = 1.00
pth_ring = 2.0

connector_size_y = 4.98

mounting_hole_offset_y = 0.25
shielding_pad_offset_y = 1.95

line_width = 0.15
crtyd_width = 0.05
crtyd_spacing = 0.5

def crtyd_round(value, direction):
	if direction > 0:
		return math.ceil(value/0.05)*0.05
	else:
		return math.floor(value/0.05)*0.05

def name(number_of_positions, shield):
	return "LSHM-1%02u-XX.X-XX-DV-A-%c-X-TR" % (number_of_positions, "S" if shield else "N")

def description(number_of_positions):
	return "Samtec %.1fmm TERMINAL/SOCKET COMBO" % (pad_pitch_x)

def tags(number_of_positions):
	return "Samtec %02ux%02u smd %.1f mm pitch terminal socket" % (
		number_of_rows,
		number_of_positions,
		pad_pitch_x)

def pad(position, x, y, diameter_pad_x, diameter_pad_y):
	return "  (pad %s smd rect (at %.3f %.3f) (size %.3f %.3f) (layers F.Cu F.Paste F.Mask))\n" % (position, x, y, diameter_pad_x, diameter_pad_y)

for shield in [True, False]:
	for number_of_positions in number_of_positions_values:
		filename = "%s.kicad_mod" % (name(number_of_positions, shield))

		x_origin = 0
		y_origin = 0

		x_start = -A(number_of_positions)/2.0
		x_end = A(number_of_positions)/2.0
		x_mid = (x_start+x_end)/2.0

		y_start = -pad_pitch_y/2.0
		y_end = pad_pitch_y/2.0

		output = open(filename, 'w')

		output.write("(module %s (layer F.Cu) (tedit %X)\n" % (name(number_of_positions, shield), int(time.time())))
		output.write("  (attr smd)\n")

		# description
		output.write("  (descr \"%s\")\n" % (description(number_of_positions)))

		# tags
		output.write("  (tags \"%s\")\n" % (tags(number_of_positions)))

		# reference
		output.write("  (fp_text reference REF** (at %.3f %.3f 270) (layer F.SilkS)\n" % (x_origin - ((C(number_of_positions) + pth_ring) if shield else E(number_of_positions))/2.0 - 1, y_origin))
		output.write("    (effects (font (size 1 1) (thickness 0.15)))\n")
		output.write("  )\n")

		#value
		output.write("  (fp_text value %s (at %.3f %.3f 270) (layer F.Fab)\n" % (name(number_of_positions, shield), x_origin + ((C(number_of_positions) + pth_ring) if shield else E(number_of_positions))/2.0 + 1, y_origin))
		output.write("    (effects (font (size 1 1) (thickness 0.15)))\n")
		output.write("  )\n")

		# pads
		for pos in range(1, number_of_positions+1):
			for row in range(1, number_of_rows+1):
				output.write(pad(2*(pos-1)+row, x_origin+x_end-(pos-1)*pad_pitch_x, y_origin+y_end-(row-1)*pad_pitch_y, pad_size_x, pad_size_y))

		# mounting holes
		mounting_holes_x = [
			x_origin - B(number_of_positions)/2.0,
			x_origin + B(number_of_positions)/2.0]
		for x in mounting_holes_x:
			output.write("  (pad \"\" np_thru_hole circle (at %.3f %.3f) (size %.3f %.3f) (drill %.3f) (layers *.Cu *.Mask))" % (
				x,
				y_origin + y_end - pad_size_y/2.0 - mounting_hole_offset_y,
				npth_drill_size,
				npth_drill_size,
				npth_drill_size));

		# shield pads
		if shield:
			for pos in ["F1","F2"]:
				x = x_origin - C(number_of_positions)/2.0 if pos == "F1" else x_origin + C(number_of_positions)/2.0
				output.write("  (pad \"%s\" thru_hole circle (at %.3f %.3f) (size %.3f %.3f) (drill %.3f) (layers *.Cu *.Mask))" % (
					pos,
					x,
					y_origin + y_end - pad_size_y/2.0 - mounting_hole_offset_y - shielding_pad_offset_y,
					pth_ring,
					pth_ring,
					pth_drill_size));

		# drawing
		x_lines = [
			x_origin - (D(number_of_positions) if shield else E(number_of_positions))/2.0,
			x_origin + x_start - pad_size_x/2.0 - line_width - 0.15,
			x_origin + x_end + pad_size_x/2.0 + line_width + 0.15,
			x_origin + (D(number_of_positions) if shield else E(number_of_positions))/2.0]

		y_lines = [
			y_origin - connector_size_y/2.0,
			y_origin + y_end - pad_size_y/2.0 - mounting_hole_offset_y - shielding_pad_offset_y - pth_ring/2.0 - line_width,
			y_origin + y_end - pad_size_y/2.0 - mounting_hole_offset_y - shielding_pad_offset_y + pth_ring/2.0 + line_width ,
			y_origin + connector_size_y/2.0]

		# top/bottom line
		for y in [y_lines[0], y_lines[-1]]:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
				x_lines[0],
				y,
				x_lines[1],
				y,
				line_width
				))
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
				x_lines[-2],
				y,
				x_lines[-1],
				y,
				line_width
				))

		if not shield:
			for x in [x_lines[0], x_lines[-1]]:
				output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
					x,
					y_lines[0],
					x,
					y_lines[-1],
					line_width
					))
		else:
			for x in [x_lines[0], x_lines[-1]]:
				output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
					x,
					y_lines[0],
					x,
					y_lines[1],
					line_width
					))
				output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.SilkS) (width %.3f))\n" % (
					x,
					y_lines[-2],
					x,
					y_lines[-1],
					line_width
					))

		# courtyard
		if not shield:
			crtyd_x_lines = [
				crtyd_round(x_lines[0] - crtyd_spacing, -1),
				crtyd_round(x_lines[-1] + crtyd_spacing, 1)]
		else:
			crtyd_x_lines = [
				crtyd_round(x_origin - C(number_of_positions)/2.0 - pth_ring/2.0 - crtyd_spacing, -1),
				crtyd_round(x_origin + C(number_of_positions)/2.0 + pth_ring/2.0 + crtyd_spacing, 1)]

		crtyd_y_lines = [
			crtyd_round(y_lines[0] - crtyd_spacing, -1),
			crtyd_round(y_lines[-1] + crtyd_spacing, 1)]

		for y in crtyd_y_lines:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				crtyd_x_lines[0],
				y,
				crtyd_x_lines[-1],
				y,
				crtyd_width))

		for x in crtyd_x_lines:
			output.write("  (fp_line (start %.3f %.3f) (end %.3f %.3f) (layer F.CrtYd) (width %.3f))\n" % (
				x,
				crtyd_y_lines[0],
				x,
				crtyd_y_lines[-1],
				crtyd_width
				))

		output.write(")\n")
		output.close()
