from header_particle_systems import *
#psf_always_emit         = 0x0000000002
#psf_global_emit_dir     = 0x0000000010
#psf_emit_at_water_level = 0x0000000020
#psf_billboard_2d        = 0x0000000100 # up_vec = dir, front rotated towards camera
#psf_billboard_3d        = 0x0000000200 # front_vec point to camera.
#psf_turn_to_velocity    = 0x0000000400
#psf_randomize_rotation  = 0x0000001000
#psf_randomize_size      = 0x0000002000
#psf_2d_turbulance       = 0x0000010000

####################################################################################################################
#   Each particle system contains the following fields:
#  
#  1) Particle system id (string): used for referencing particle systems in other files.
#     The prefix psys_ is automatically added before each particle system id.
#  2) Particle system flags (int). See header_particle_systems.py for a list of available flags
#  3) mesh-name.
####
#  4) Num particles per second:    Number of particles emitted per second.
#  5) Particle Life:    Each particle lives this long (in seconds).
#  6) Damping:          How much particle's speed is lost due to friction.
#  7) Gravity strength: Effect of gravity. (Negative values make the particles float upwards.)
#  8) Turbulance size:  Size of random turbulance (in meters)
#  9) Turbulance strength: How much a particle is affected by turbulance.
####
# 10,11) Alpha keys :    Each attribute is controlled by two keys and 
# 12,13) Red keys   :    each key has two fields: (time, magnitude)
# 14,15) Green keys :    For example scale key (0.3,0.6) means 
# 16,17) Blue keys  :    scale of each particle will be 0.6 at the
# 18,19) Scale keys :    time 0.3 (where time=0 means creation and time=1 means end of the particle)
#
# The magnitudes are interpolated in between the two keys and remain constant beyond the keys.
# Except the alpha always starts from 0 at time 0.
####
# 20) Emit Box Size :   The dimension of the box particles are emitted from.
# 21) Emit velocity :   Particles are initially shot with this velocity.
# 22) Emit dir randomness
# 23) Particle rotation speed: Particles start to rotate with this (angular) speed (degrees per second).
# 24) Particle rotation damping: How quickly particles stop their rotation
####################################################################################################################

particle_systems = [
	("game_rain", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prtcl_rain",
		500.0, 0.5, 0.33, 1.0, 10.0, 0.0,
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(8.2, 8.2, 0.2),
		(0.0, 0.0, -10.0),
		0.0,
		0,
		0.5
	),

	("game_snow", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_snow_fall_1",
		150.0, 2.0, 0.2, 0.1, 30.0, 20.0,
		(0.2, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(10.0, 10.0, 0.5),
		(0.0, 0.0, -5.0),
		1.0,
		200,
		0.5
	),
# Required:


   ("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     5000, 5.65, 3, 0.9, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),          #alpha keys
     (0.1, 0.9), (1, 0.9),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.1, 0.02),   (1, 0.15),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.6, 1.1, 1.2),                #emit velocity

     0,                       #emit dir randomness
     0,                         #rotation speed

     0,                         #rotation damping
    ),

    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",

     5000, 0.8, 3, 1.1, 10, 10,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.6), (1, 0.01),          #alpha keys
     (0.1, 0.5), (1, 0.7),      #red keys
     (0.1, 0.5), (1, 0.7),       #green keys
     (0.1, 0.5), (1, 0.7),      #blue keys
     (0.1, 0.1),   (1, 0.75),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0.9, 0.1, 0.2 ),                #emit velocity



     0.9,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),

	("game_hoof_dust", psf_billboard_3d|psf_randomize_rotation|psf_randomize_size|psf_2d_turbulance, "prt_mesh_dust_1",
		5.0, 2.0, 10.0, 0.05, 10.0, 39.0,
		(0.2, 0.5), (1.0, 0.0),
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.9), (1.0, 0.9),
		(0.0, 0.78), (1.0, 0.78),
		(0.0, 2.0), (1.0, 3.5),
		(0.2, 0.3, 0.2),
		(0.0, 0.0, 3.9),
		0.5,
		130,
		0.5
	),

#	("game_hoof_dust_snow", psf_billboard_3d|psf_randomize_size, "prt_mesh_snow_dust_1",
#		6.0, 2.0, 3.5, 1.0, 10.0, 0.0,
#		(0.2, 1.0), (1.0, 1.0),
#		(0.0, 1.0), (1.0, 1.0),
#		(0.0, 1.0), (1.0, 1.0),
#		(0.0, 1.0), (1.0, 1.0),
#		(0.5, 4.0), (1.0, 5.7),
#		(0.2, 1.0, 0.1),
#		(0.0, 0.0, 1.0),
#		2.0,
#		0,
#		0.0
#	),

	("game_hoof_dust_mud", psf_billboard_2d|psf_randomize_rotation|psf_randomize_size|psf_2d_turbulance, "prt_mesh_dust_1",
		5.0, 0.7, 10.0, 3.0, 0.0, 0.0,
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.7), (1.0, 0.7),
		(0.0, 0.6), (1.0, 0.6),
		(0.0, 0.4), (1.0, 0.4),
		(0.0, 0.2), (1.0, 0.22),
		(0.15, 0.5, 0.1),
		(0.0, 0.0, 15.0),
		6.0,
		200,
		0.5
	),

	("game_water_splash_1", psf_emit_at_water_level|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_drop",
		20.0, 0.85, 0.25, 0.9, 10.0, 0.0,
		(0.3, 0.5), (1.0, 0.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 0.3), (1.0, 0.18),
		(0.3, 0.2, 0.1),
		(0.0, 1.2, 2.3),
		0.3,
		50,
		0.5
	),

	("game_water_splash_2", psf_emit_at_water_level|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_splash_b",
		30.0, 0.4, 0.7, 0.5, 10.0, 0.0,
		(0.3, 1.0), (1.0, 0.3),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 0.25), (1.0, 0.7),
		(0.4, 0.3, 0.1),
		(0.0, 1.3, 1.1),
		0.1,
		50,
		0.5
	),

	("game_water_splash_3", psf_emit_at_water_level, "prt_mesh_water_wave_1",
		5.0, 2.0, 0.0, 0.0, 10.0, 0.0,
		(0.03, 0.2), (1.0, 0.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 3.0), (1.0, 10.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 0.0),
		0.0,
		0,
		0.5
	),

	("torch_fire", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		50.0, 0.35, 0.2, 0.03, 10.0, 0.0,
		(0.5, 0.8), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.7), (1.0, 0.3),
		(0.5, 0.2), (1.0, 0.0),
		(0.0, 0.15), (0.4, 0.3),
		(0.04, 0.04, 0.01),
		(0.0, 0.0, 0.5),
		0.0,
		200,
		0.5
	),

	("fire_glow_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_fire_2",
		2.0, 0.55, 0.2, 0.0, 10.0, 0.0,
		(0.5, 0.9), (1.0, 0.0),
		(0.0, 0.9), (1.0, 0.9),
		(0.0, 0.7), (1.0, 0.7),
		(0.0, 0.4), (1.0, 0.4),
		(0.0, 2.0), (1.0, 2.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 0.0),
		0.0,
		0,
		0.0
	),

	("fire_glow_fixed", psf_global_emit_dir|psf_billboard_3d, "prt_mesh_fire_2",
		4.0, 100.0, 0.2, 0.0, 10.0, 0.0,
		(-0.01, 1.0), (1.0, 1.0),
		(0.0, 0.9), (1.0, 0.9),
		(0.0, 0.7), (1.0, 0.7),
		(0.0, 0.4), (1.0, 0.4),
		(0.0, 2.0), (1.0, 2.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 0.0),
		0.0,
		0,
		0.0
	),

	("torch_smoke", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prtcl_dust_a",
		15.0, 0.5, 0.2, -0.2, 10.0, 0.1,
		(0.5, 0.25), (1.0, 0.0),
		(0.0, 0.2), (1.0, 0.1),
		(0.0, 0.2), (1.0, 0.09),
		(0.0, 0.2), (1.0, 0.08),
		(0.0, 0.5), (0.8, 2.5),
		(0.1, 0.1, 0.1),
		(0.0, 0.0, 1.5),
		0.1,
		0,
		0.0
	),

	("flue_smoke_short", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
		15.0, 1.5, 0.1, -0.0, 10.0, 12.0,
		(0.0, 0.3), (1.0, 0.0),
		(0.0, 0.2), (1.0, 0.1),
		(0.0, 0.2), (1.0, 0.09),
		(0.0, 0.2), (1.0, 0.08),
		(0.0, 1.5), (1.0, 7.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 1.5),
		0.1,
		150,
		0.8
	),

	("flue_smoke_tall", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
		15.0, 3.0, 0.5, -0.0, 15.0, 12.0,
		(0.0, 0.35), (1.0, 0.0),
		(0.0, 0.3), (1.0, 0.1),
		(0.0, 0.3), (1.0, 0.1),
		(0.0, 0.3), (1.0, 0.1),
		(0.0, 2.0), (1.0, 7.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 1.5),
		0.1,
		150,
		0.5
	),

	("war_smoke_tall", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		5.0, 12.0, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 2.2), (1.0, 15.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 2.2),
		0.1,
		100,
		0.2
	),

	("ladder_dust_6m", psf_billboard_3d, "prt_mesh_smoke_1",
		700.0, 0.9, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 2.0),
		(0.75, 0.75, 3.5),
		(0.0, 0.0, 0.0),
		0.1,
		100,
		0.2
	),

	("ladder_dust_8m", psf_billboard_3d, "prt_mesh_smoke_1",
		900.0, 0.9, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 2.0),
		(0.75, 0.75, 4.5),
		(0.0, 0.0, 0.0),
		0.1,
		100,
		0.2
	),

	("ladder_dust_10m", psf_billboard_3d, "prt_mesh_smoke_1",
		1100.0, 0.9, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 2.0),
		(0.75, 0.75, 5.5),
		(0.0, 0.0, 0.0),
		0.1,
		100,
		0.2
	),

	("ladder_dust_12m", psf_billboard_3d, "prt_mesh_smoke_1",
		1300.0, 0.9, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 2.0),
		(0.75, 0.75, 6.5),
		(0.0, 0.0, 0.0),
		0.1,
		100,
		0.2
	),

	("ladder_dust_14m", psf_billboard_3d, "prt_mesh_smoke_1",
		1500.0, 0.9, 0.0, 0.0, 7.0, 7.0,
		(0.0, 0.25), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 0.8),
		(0.0, 1.0), (1.0, 2.0),
		(0.75, 0.75, 7.5),
		(0.0, 0.0, 0.0),
		0.1,
		100,
		0.2
	),

	("ladder_straw_6m", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		700.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.75, 0.75, 3.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("ladder_straw_8m", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		900.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.75, 0.75, 4.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("ladder_straw_10m", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		1100.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.75, 0.75, 5.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("ladder_straw_12m", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		1300.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.75, 0.75, 6.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("ladder_straw_14m", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		1500.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.75, 0.75, 7.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("torch_fire_sparks", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
		10.0, 0.7, 0.2, 0.0, 10.0, 0.02,
		(0.66, 1.0), (1.0, 0.0),
		(0.1, 0.7), (1.0, 0.7),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.1), (1.0, 0.1),
		(0.1, 0.05), (1.0, 0.05),
		(0.1, 0.1, 0.1),
		(0.0, 0.0, 0.9),
		0.0,
		0,
		0.0
	),

	("fire_sparks_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
		10.0, 1.5, 0.2, 0.0, 3.0, 10.0,
		(0.6, 1.0), (1.0, 1.0),
		(0.1, 0.7), (1.0, 0.7),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.1), (1.0, 0.1),
		(0.1, 0.07), (1.0, 0.03),
		(0.17, 0.17, 0.01),
		(0.0, 0.0, 1.0),
		0.0,
		0,
		0.0
	),

	("pistol_smoke", psf_billboard_3d, "prtcl_dust_a",
		90.0, 2.5, 0.6, -0.2, 60.0, 1.5,
		(0.0, 0.75), (1.0, 0.0),
		(0.0, 0.7), (1.0, 0.4),
		(0.0, 0.7), (1.0, 0.4),
		(0.0, 0.7), (1.0, 0.4),
		(0.0, 1.5), (0.5, 11.0),
		(0.1, 0.1, 0.1),
		(2.0, 2.0, 0.0),
		0.1,
		0,
		0.0
	),

	("brazier_fire_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		25.0, 0.5, 0.1, 0.0, 10.0, 0.0,
		(0.5, 0.4), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.7), (1.0, 0.3),
		(0.5, 0.2), (1.0, 0.0),
		(0.1, 0.2), (1.0, 0.5),
		(0.1, 0.1, 0.01),
		(0.0, 0.0, 0.4),
		0.0,
		100,
		0.2
	),

	("cooking_fire_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		25.0, 0.35, 0.1, 0.03, 10.0, 0.0,
		(0.5, 0.8), (1.0, 0.0),
		(0.5, 0.5), (1.0, 0.27),
		(0.5, 0.35), (1.0, 0.09),
		(0.5, 0.1), (1.0, 0.0),
		(0.1, 0.5), (1.0, 1.0),
		(0.05, 0.05, 0.01),
		(0.0, 0.0, 1.0),
		0.0,
		200,
		0.0
	),

	("cooking_smoke", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		4.0, 4.0, 0.1, 0.0, 3.0, 5.0,
		(0.2, 0.2), (1.0, 0.0),
		(0.0, 0.8), (1.0, 1.0),
		(0.0, 0.8), (1.0, 1.0),
		(0.0, 0.85), (1.0, 1.0),
		(0.0, 0.65), (1.0, 3.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 1.2),
		0.0,
		0,
		0.0
	),

	("food_steam", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
		3.0, 1.0, 0.0, 0.0, 8.0, 1.0,
		(0.5, 0.1), (1.0, 0.0),
		(0.0, 1.0), (1.0, 0.1),
		(0.0, 1.0), (1.0, 0.1),
		(0.0, 1.0), (1.0, 0.1),
		(0.0, 0.2), (0.9, 0.5),
		(0.05, 0.05, 0.0),
		(0.0, 0.0, 0.1),
		0.0,
		100,
		0.5
	),

	("candle_light", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_candle_fire_1",
		7.0, 1.1, 0.6, -0.0, 10.0, 0.2,
		(0.1, 0.5), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.6), (1.0, 0.1),
		(0.5, 0.2), (1.0, 0.0),
		(0.3, 0.2), (1.0, 0.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 0.09),
		0.0,
		0,
		0.0
	),

	("candle_light_small", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_candle_fire_1",
		4.0, 1.1, 0.6, -0.0, 10.0, 0.2,
		(0.1, 0.8), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.6), (1.0, 0.1),
		(0.5, 0.2), (1.0, 0.0),
		(0.3, 0.13), (1.0, 0.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 0.06),
		0.0,
		0,
		0.0
	),

	("lamp_fire", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		10.0, 0.8, 0.6, -0.0, 10.0, 0.4,
		(0.1, 0.5), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.8), (1.0, 0.1),
		(0.5, 0.4), (1.0, 0.0),
		(0.3, 0.35), (0.9, 0.5),
		(0.01, 0.01, 0.0),
		(0.0, 0.0, 0.35),
		0.03,
		100,
		0.5
	),

	("dummy_smoke", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
		500.0, 3.0, 15.0, -0.05, 10.0, 0.2,
		(0.1, 0.5), (1.0, 0.0),
		(0.1, 0.8), (1.0, 0.8),
		(0.1, 0.7), (1.0, 0.7),
		(0.1, 0.6), (1.0, 0.7),
		(0.0, 0.7), (1.0, 2.2),
		(0.2, 0.2, 0.5),
		(0.0, 0.0, 0.05),
		2.0,
		10,
		0.1
	),

#Dummy straw was moved from here patched to an extent
	("dummy_smoke_big", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
		500.0, 9.0, 15.0, -0.05, 10.0, 0.2,
		(0.1, 0.9), (1.0, 0.0),
		(0.1, 0.8), (1.0, 0.8),
		(0.1, 0.7), (1.0, 0.7),
		(0.1, 0.6), (1.0, 0.7),
		(0.0, 5.0), (1.0, 15.0),
		(3.0, 3.0, 5.0),
		(0.0, 0.0, 0.05),
		2.0,
		10,
		0.1
	),
#Dummy straw big was moved from here patched to an extent
	("gourd_smoke", psf_billboard_3d|psf_randomize_size, "prt_mesh_dust_1",
		500.0, 3.0, 15.0, -0.05, 10.0, 0.2,
		(0.1, 0.5), (1.0, 0.0),
		(0.1, 0.8), (1.0, 0.8),
		(0.1, 0.7), (1.0, 0.7),
		(0.1, 0.6), (1.0, 0.7),
		(0.0, 0.5), (1.0, 1.0),
		(0.2, 0.2, 0.5),
		(0.0, 0.0, 0.05),
		2.0,
		10,
		0.1
	),

	("gourd_piece_1", psf_randomize_rotation, "prt_gourd_piece_1",
		15.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 1.0), (1.0, 1.0),
		(0.2, 0.2, 0.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("gourd_piece_2", psf_randomize_rotation|psf_randomize_size, "prt_gourd_piece_2",
		50.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 1.0), (1.0, 1.0),
		(0.2, 0.2, 0.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),

	("fire_fly_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_sparks_mesh_1",
		2.0, 5.0, 1.2, 0.0, 50.0, 7.0,
		(0.1, 0.8), (1.0, 0.2),
		(0.5, 0.7), (1.0, 0.7),
		(0.5, 0.8), (1.0, 0.8),
		(0.5, 1.0), (1.0, 1.0),
		(0.0, 0.1), (1.0, 0.1),
		(20.0, 20.0, 0.5),
		(0.0, 0.0, 0.0),
		5.0,
		0,
		0.0
	),

	("bug_fly_1", psf_always_emit|psf_billboard_2d, "prt_mesh_rose_a",
		20.0, 8.0, 0.02, 0.025, 1.0, 5.0,
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.25), (1.0, 0.25),
		(10.0, 5.0, 0.1),
		(0.0, 0.0, -0.9),
		0.01,
		10,
		0.0
	),

	("moon_beam_1", psf_always_emit|psf_global_emit_dir|psf_billboard_2d|psf_randomize_size, "prt_mesh_moon_beam",
		2.0, 4.0, 1.2, 0.0, 0.0, 0.0,
		(0.5, 1.0), (1.0, 0.0),
		(0.0, 0.4), (1.0, 0.4),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.6), (1.0, 0.6),
		(0.0, 2.0), (1.0, 2.2),
		(1.0, 1.0, 0.2),
		(0.0, 0.0, -2.0),
		0.0,
		100,
		0.5
	),

	("moon_beam_paricle_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_size, "prt_sparks_mesh_1",
		10.0, 1.5, 1.5, 0.0, 10.0, 10.0,
		(0.5, 1.0), (1.0, 0.0),
		(0.5, 0.5), (1.0, 0.5),
		(0.5, 0.7), (1.0, 0.7),
		(0.5, 1.0), (1.0, 1.0),
		(0.0, 0.1), (1.0, 0.1),
		(1.0, 1.0, 4.0),
		(0.0, 0.0, 0.0),
		0.5,
		0,
		0.0
	),

	("night_smoke_1", psf_always_emit|psf_global_emit_dir|psf_billboard_3d, "prt_mesh_dust_1",
		5.0, 10.0, 1.5, 0.0, 50.0, 2.0,
		(0.3, 0.1), (1.0, 0.0),
		(0.5, 0.5), (1.0, 0.5),
		(0.5, 0.5), (1.0, 0.5),
		(0.5, 0.5), (1.0, 0.6),
		(0.0, 10.0), (1.0, 10.0),
		(25.0, 25.0, 0.5),
		(0.0, 1.0, 0.0),
		2.0,
		20,
		1.0
	),

	("fireplace_fire_small", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		25.0, 0.8, 0.2, -0.1, 10.0, 0.0,
		(0.5, 0.5), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.7), (1.0, 0.3),
		(0.5, 0.2), (1.0, 0.0),
		(0.0, 0.2), (1.0, 0.7),
		(0.2, 0.1, 0.01),
		(0.0, 0.0, 0.2),
		0.1,
		100,
		0.5
	),

	("fireplace_fire_big", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		35.0, 0.6, 0.2, -0.2, 10.0, 0.0,
		(0.5, 0.5), (1.0, 0.0),
		(0.5, 1.0), (1.0, 0.9),
		(0.5, 0.7), (1.0, 0.3),
		(0.5, 0.2), (1.0, 0.0),
		(0.0, 0.4), (1.0, 1.0),
		(0.4, 0.2, 0.01),
		(0.0, 0.0, 0.4),
		0.1,
		100,
		0.5
	),

	("village_fire_big", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		50.0, 1.0, 0.0, -1.2, 25.0, 10.0,
		(0.2, 0.7), (1.0, 0.0),
		(0.2, 1.0), (1.0, 0.9),
		(0.2, 0.7), (1.0, 0.3),
		(0.2, 0.2), (1.0, 0.0),
		(0.0, 2.0), (1.0, 6.0),
		(2.2, 2.2, 0.2),
		(0.0, 0.0, 0.0),
		0.0,
		250,
		0.3
	),

	("village_fire_smoke_big", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		30.0, 2.0, 0.3, -1.0, 50.0, 10.0,
		(0.5, 0.15), (1.0, 0.0),
		(0.2, 0.4), (1.0, 0.2),
		(0.2, 0.4), (1.0, 0.2),
		(0.2, 0.4), (1.0, 0.2),
		(0.0, 6.0), (1.0, 8.0),
		(2.0, 2.0, 1.0),
		(0.0, 0.0, 5.0),
		0.0,
		0,
		0.1
	),

	("map_village_fire", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
		20.0, 1.0, 0.0, -0.2, 3.0, 3.0,
		(0.2, 0.7), (1.0, 0.0),
		(0.2, 1.0), (1.0, 0.9),
		(0.2, 0.7), (1.0, 0.3),
		(0.2, 0.2), (1.0, 0.0),
		(0.0, 0.15), (1.0, 0.45),
		(0.2, 0.2, 0.02),
		(0.0, 0.0, 0.0),
		0.0,
		250,
		0.3
	),

	("map_village_fire_smoke", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		25.0, 2.5, 0.3, -0.15, 3.0, 3.0,
		(0.5, 0.15), (1.0, 0.0),
		(0.2, 0.4), (1.0, 0.3),
		(0.2, 0.4), (1.0, 0.3),
		(0.2, 0.4), (1.0, 0.3),
		(0.0, 0.6), (1.0, 0.9),
		(0.2, 0.2, 0.1),
		(0.0, 0.0, 0.03),
		0.0,
		0,
		0.1
	),

	("map_village_looted_smoke", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		20.0, 3.0, 0.3, -0.11, 3.0, 2.0,
		(0.5, 0.15), (1.0, 0.0),
		(0.2, 0.5), (1.0, 0.5),
		(0.2, 0.5), (1.0, 0.5),
		(0.2, 0.5), (1.0, 0.5),
		(0.0, 0.7), (1.0, 1.3),
		(0.2, 0.2, 0.1),
		(0.0, 0.0, 0.015),
		0.0,
		0,
		0.1
	),

	("dungeon_water_drops", psf_always_emit|psf_global_emit_dir|psf_billboard_2d, "prtcl_rain",
		1.0, 1.0, 0.33, 0.8, 0.0, 0.0,
		(1.0, 0.2), (1.0, 0.2),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 0.8), (1.0, 0.8),
		(0.05, 0.05, 0.5),
		(0.0, 0.0, -5.0),
		0.0,
		0,
		0.0
	),

	("wedding_rose", psf_always_emit|psf_billboard_2d, "prt_mesh_rose_a",
		50.0, 8.0, 0.02, 0.025, 1.0, 5.0,
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.25), (1.0, 0.25),
		(4.0, 4.0, 0.1),
		(0.0, 0.0, -0.9),
		0.01,
		10,
		0.0
	),

	("sea_foam_a", psf_always_emit|psf_turn_to_velocity|psf_randomize_size, "prt_foam_a",
		1.0, 3.0, 1.0, 0.0, 0.0, 0.0,
		(0.7, 0.1), (1.0, 0.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 4.0), (1.0, 4.5),
		(10.0, 1.0, 0.0),
		(0.0, 1.0, 0.0),
		0.0,
		0,
		0.5
	),

	("fall_leafs_a", psf_always_emit|psf_billboard_2d, "prt_mesh_yrellow_leaf_a",
		1.0, 9.0, 0.0, 0.025, 4.0, 4.0,
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.5), (1.0, 0.5),
		(0.0, 0.25), (1.0, 0.25),
		(4.0, 4.0, 4.0),
		(0.0, 0.01, -0.9),
		0.02,
		15,
		0.0
	),

	("desert_storm", psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_dust_1",
		250.0, 2.0, 1.0, -0.15, 20.0, 40.0,
		(0.2, 0.5), (1.0, 0.0),
		(0.0, 1.0), (1.0, 1.0),
		(0.0, 0.9), (1.0, 0.9),
		(0.0, 0.78), (1.0, 0.78),
		(0.0, 20.0), (1.0, 45.5),
		(40.0, 40.0, 5.0),
		(-20.0, 0.0, 3.0),
		0.0,
		130,
		0.5
	),

	("blizzard", psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_dust_1",
		250.0, 7.0, 1.0, 0.45, 20.0, 40.0,
		(0.2, 0.5), (1.0, 0.5),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 30.0), (1.0, 45.5),
		(35.0, 35.0, 8.0),
		(-35.0, 0.0, -8.0),
		0.0,
		130,
		0.5
	),

	("rain", psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_dust_1",
		400.0, 5.0, 1.0, 0.65, 20.0, 40.0,
		(1.0, 0.3), (1.0, 0.3),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(1.0, 1.0), (1.0, 1.0),
		(0.0, 20.0), (1.0, 45.5),
		(35.0, 35.0, 8.0),
		(-20.0, 0.0, -10.0),
		0.0,
		130,
		0.5
	),

	("oil", psf_always_emit|psf_global_emit_dir|psf_billboard_3d|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
		30.0, 4.0, 0.1, 1.0, 3.0, 5.0,
		(0.2, 0.7), (1.0, 2.0),
		(0.0, 0.2), (1.0, 0.0),
		(0.0, 0.2), (1.0, 0.0),
		(0.0, 0.2), (1.0, 0.0),
		(0.0, 0.65), (1.0, 3.0),
		(0.0, 0.0, 0.0),
		(0.0, 0.0, 1.2),
		0.0,
		0,
		0.0
	),
#New particles from CWE
    ("ship_shrapnel", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
    5000, 1, 2, 1.5, 10, 2,
    (0.1, 1), (1, 1),
    (0.1, 0.6), (1, 0.6),
    (0.1, 0.5), (1, 0.5),
    (0.1, 0.4), (1, 0.4),
    (0, 1.5), (5, 1.5),
    (2, 2, 5),
    (0, 0, 0),
    2.3,
    200, 0
  ),
  ("lanse", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
    2000, 3, 2, 0.7, 10, 2,
    (0.1, 1), (1, 1),
    (0.1, 0.6), (1, 0.6),
    (0.1, 0.5), (1, 0.5),
    (0.1, 0.4), (1, 0.4),
    (0, 0.8), (1, 0.8),
    (2.5, 2.5, 2.5),
    (0, 0, 0),
    2.3,
    200, 0
  ),
  
  ("lanse_straw", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
    2000, 3, 2, 0.7, 10, 2,
    (0.1, 1), (1, 1),
    (0.1, 0.6), (1, 0.6),
    (0.1, 0.5), (1, 0.5),
    (0.1, 0.4), (1, 0.4),
    (0, 0.8), (1, 0.8),
    (2.5, 2.5, 2.5),
    (0, 0, 0),
    2.3,
    200, 0
  ),

  	("dummy_straw", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		500.0, 1.0, 2.0, 0.9, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.3), (1.0, 0.3),
		(0.2, 0.2, 0.5),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),
	
	  ("dummy_straw_big", psf_randomize_rotation|psf_randomize_size, "prt_mesh_straw_1",
		500.0, 3.0, 2.0, 2.0, 10.0, 2.0,
		(0.1, 1.0), (1.0, 1.0),
		(0.1, 0.6), (1.0, 0.6),
		(0.1, 0.5), (1.0, 0.5),
		(0.1, 0.4), (1.0, 0.4),
		(0.0, 0.8), (1.0, 0.8),
		(3.0, 3.0, 3.0),
		(0.0, 0.0, 0.0),
		2.3,
		200,
		0.0
	),
	
	
  ("lanse_blood", psf_billboard_3d|psf_billboard_drop|psf_randomize_rotation|psf_randomize_size, "prt_mesh_blood_3",
    2000, 0.6, 3, 0.3, 0, 0,
    (0, 0.25), (0.7, 0.1),
    (0.1, 0.7), (1, 0.7),
    (0.1, 0.7), (1, 0.7),
    (0.1, 0.7), (1, 0.7),
    (0.1, 0.4), (0.5, 0.35),
    (1.2, 1.2, 1.2),
    (0.4, 0.4, 0),
    0.3,
    150, 0
  ),
	#End new particles
	
	    ("blood_decapitation", psf_billboard_3d|psf_billboard_drop|psf_randomize_rotation|psf_randomize_size, "prt_blood_decapitation", #here
    2000, 0.6, 3, 0.3, 0, 0,
    (0, 0.25), (0.7, 0.1),
    (0.1, 0.7), (1, 0.7),
    (0.1, 0.7), (1, 0.7),
    (0.1, 0.7), (1, 0.7),
    (0, 0.15), (1, 0.35),
    (0.01, 0.2, 0.01),
    (0.2, 0.3, 0),
    0.3,
    150, 0
  ),
  #End new particles
]