$fn = 360;
medida = 0.3*25.4;
//translate([(medida-5.4)/2,(medida-5)/2,0])
translate([-2.7,-2.5,0])
{
  union()
  {
    difference() {
      translate([0.2,0,0])
        cube([5,5,1.6]);
      translate([0.2,0,0])
        cube([1,5,0.5]);
        translate([4.2,0,0])
          cube([1,5,0.5]);
      translate([2.7, 2.5, 1.4])
      {
        cylinder(r1=1.8, r2=2, h=0.3);
      }
    }
    for (i=[0:1]) {
      for (j=[0:1]) {
        translate([4.4*i,0.4+(3.2*j),0])
        cube([1,1,0.5]);
      }
    }
  }
}
