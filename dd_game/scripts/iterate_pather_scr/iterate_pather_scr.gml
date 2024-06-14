/// @function scr_iterate_pather(coords, grid, current_area)
/// @description peepee
/// @param {array} coords
/// @param {grid} grid
/// @param {map_area_obj} current_area

var coords = argument0;
var grid = argument1;
var current_area = argument2;
var grid_size = array_height_2d(grid);

var offsets = ds_list_create();
offsets[| 0] = [-1, 0];
offsets[| 1] = [1, 0];
offsets[| 2] = [0, -1];
offsets[| 3] = [0, 1];
offsets[| 4] = [1, -1];
offsets[| 5] = [-1, 1];
ds_list_shuffle(offsets);

var new_coords;
for (var i = 0; i < 6; i++) {
	var offset = offsets[| i];
	new_coords[0] = coords[0] + offset[0];
	new_coords[1] = coords[1] + offset[1];
	if not is_inside_grid_scr(new_coords, grid_size) {
		continue;
	}
	var grid_element = grid[new_coords[0], new_coords[1]]
	if grid_element != noone {
		ds_list_add(current_area.neighbours, grid_element)
		ds_list_add(grid_element.neighbours, current_area)
		draw_path_scr(
			current_area.x,
			current_area.y,
			grid_element.x,
			grid_element.y
		);
		continue;
	}
	coords[@0] = new_coords[0];
	coords[@1] = new_coords[1];
	return true;
}
return false;
