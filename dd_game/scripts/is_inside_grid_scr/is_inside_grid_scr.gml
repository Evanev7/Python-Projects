/// @function scr_is_inside_grid(coords, grid_size)
/// @description peepee
/// @param {array} coords
/// @param {int} grid_size

var coords = argument0;
var grid_size = argument1;

if coords[0] < 0 or coords[1] < 0 or coords[0] >= grid_size or coords[1] >= grid_size {
	return false;
}

var added = coords[0] + coords[1];
// Same as (grid_size - 1) div 2
// Bitwise shift right once to divide by 2
// Don't have to subtract as rightmost bit is truncated
var delta = grid_size >> 1
if added < delta or added >= grid_size + delta {
	return false;
}

return true;
