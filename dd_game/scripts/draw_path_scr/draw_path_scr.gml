/// @function scr_draw_path(x1, y1, x2, y2)
/// @description Draw a path between two areas
/// @param {real} instance_id The unique instance ID value of the instance to check.
/// @param {real} instance_id The unique instance ID value of the instance to check.

step_list = [];

x1 = argument0;
y1 = argument1;
x2 = argument2;
y2 = argument3;

Euclid_dist = point_distance(x1,y1,x2,y2);
spacing = (Euclid_dist mod 32)/2;
angle = arctan2((y2-y1), (x2-x1));

test_button_obj.image_angle = Euclid_dist

x_addition =  32 * cos(angle);
y_addition =  32 * sin(angle);

start_x = x1 + spacing * cos(angle);
start_y = y1 + spacing * sin(angle);

for (var i = 0; i<(Euclid_dist div 32); i++){

	step_list[i] = instance_create_layer(start_x + i*x_addition, start_y + i*y_addition, "map", path_obj);	
	step_list[i].image_angle = 360 - radtodeg(angle);
	
}

return step_list;

