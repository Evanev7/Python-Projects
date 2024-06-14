if (clicked == true) {
	
	for (i=0; i<array_length_1d(step_list); i++){
		instance_destroy(step_list[i]);
	}
	
	step_list = draw_path_scr(x, y, mouse_x, mouse_y);
	
}