if mouse_check_button_pressed(mb_left) {
	// Get area instance that the user clicks on
	var inst = instance_position(mouse_x, mouse_y, map_area_obj);
	if instance_exists(inst) {
		if current_area == noone {
			// If the player is not on an area, let them move anywhere
			// This is a shitty temporary fix because the player starts outside
			target_inst = inst;
			has_target = true;
			// Instantly sets his area to the target area, another quick fix
			current_area = target_inst;
		} else if not has_target {
			// Iterate through the neighbours of the current area
			// Check that the clicked area is one of the neighbours
			var n_neighbours = ds_list_size(current_area.neighbours);
			for (var i = 0; i < n_neighbours; i++) {
				var neighbour = current_area.neighbours[| i];
				if inst == neighbour {
					target_inst = inst;
					has_target = true;
				}
			}
		}
	}
}

if has_target {
	// Move towards target at 5px / frame
	// If closer than 5px to target, then move the distance required
	// This prevents overshooting and bouncing back and forth
	distance = point_distance(x, y, target_inst.x, target_inst.y);
	move_towards_point(target_inst.x, target_inst.y, min(5, distance));
	// If reached target then reset stuff
	if x == target_inst.x and y == target_inst.y {
		current_area = target_inst;
		target_inst = noone;
		has_target = false;
	}
}

