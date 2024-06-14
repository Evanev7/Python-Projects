// Ensure only one instance exists
if instance_number(object_index) > 1 {
	instance_destroy()
	exit
}

// Create map screen obejct
instance_create_layer(window_get_width() / 2, window_get_height(), "map", map_screen_obj)

areas = ds_list_create();

// randomise rng seed value
randomize();

var n_area = 20;
// Make grid_size large enough to fit all areas with room to spare
var grid_size = ceil(1.5 * sqrt(n_area)) + 1;
// The entire grid is offset by this in pixel in the game screen
var offset = [50, 50];

// Grid side lengths must be odd so that hexagon is regular
if grid_size mod 2 == 0 {
	grid_size--;
}

// Initialise grid as empty
var grid;
for (var i=0; i < grid_size; i++) {
	for (var j=0; j < grid_size; j++) {
		grid[i, j] = noone;
	}
}

// The first area must be added by hand as the
// stepping algorithm needs a jumping off point
var coords = [0, grid_size >> 1];
// coord_history is a chronological list of seen nodes, can be popped off to backtrack
var coord_history = ds_list_create();
ds_list_add(coord_history, [coords[0], coords[1]]);
// Offset the x direction by the y coordinate to get a hexagonal grid
var area = instance_create_layer(
	offset[0] + coords[0] * 100 + coords[1] * 50,
	offset[1] + coords[1] * 100,
	"map",
	map_area_obj)
grid[coords[0], coords[1]] = area;
ds_list_add(areas, area);

var n_placed_area = 1;
while n_placed_area < n_area {
	// using current coords, iterate to get the new coords
	if iterate_pather_scr(coords, grid, area) {
		n_placed_area++;
		ds_list_add(coord_history, [coords[0], coords[1]]);
		// Keep track of previous area to add a link between it and the new one
		var prev_area = area;
		var area = instance_create_layer(
			offset[0] + coords[0] * 100 + coords[1] * 50,
			offset[1] + coords[1] * 100,
			"map",
			map_area_obj);
		// Add bi-directional link
		ds_list_add(area.neighbours, prev_area);
		ds_list_add(prev_area.neighbours, area);
		draw_path_scr(
			area.x,
			area.y,
			prev_area.x,
			prev_area.y
		);
		grid[coords[0], coords[1]] = area;
		ds_list_add(areas, area);
	} else {
		// If there is no possible movement, backtrack
		// through the history and try again
		var size = ds_list_size(coord_history);
		ds_list_delete(coord_history, size - 1);
		coords = coord_history[| size - 2];
		coords[0] *= 1;
		area = grid[coords[0], coords[1]];
	}
}
