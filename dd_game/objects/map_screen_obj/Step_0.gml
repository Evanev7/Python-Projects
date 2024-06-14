/// @description Activate/Deactivate map screen

// If tab key pressed
if keyboard_check_pressed(vk_tab) {
	
	// Update movement status
	if hud_status == "down" {
		hud_status = "moving"
		hud_multiplier = -1
	} else if hud_status == "up" {
		hud_status = "moving"
		hud_multiplier = 1
	} else {
		hud_multiplier = -hud_multiplier
	}
}

// Handle map speed in oddly specific ways
if hud_status == "moving" {
	hud_velocity = (y/2-20)
	if hud_multiplier == 1 {
		hud_velocity += (720-y)/20
	} else if y > 200 {
		hud_velocity = 80
	}
	
	if y <= 40 and hud_multiplier == -1 {
		hud_velocity = 0
		hud_status = "up"
	} else if y >= 720 and hud_multiplier == 1 { 
		y=720
		hud_velocity = 0
		hud_status = "down"
	}

	vspeed = hud_velocity * hud_multiplier
}