/// @function scr_iterate_pather(coord_list)
/// @description peepee
/// @param {ds_list -> array} coords_list

var out_string = "";
var coord_list = argument0;
var n_coords = ds_list_size(coord_list);
for (var i = 0; i < n_coords; i++) {
	var coord = coord_list[| i];
	out_string = out_string + ", [" + string(coord[0]) + ", " + string(coord[1]) + "]";
}
show_debug_message(out_string);
