extends Node3D

@export var delta_x: float
@export var delta_y: float
@export var delta_z: float

@export var size: float

@export var default_alpha: float
@export var starting_temp: float

var voxelArray:Array

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	var space_state = get_world_3d().direct_space_state
	for x in size:
		for y in size:
			for z in size:
				var params = PhysicsRayQueryParameters3D.create(Vector3(x,y,z),Vector3(x + 0.01,y + 0.01 ,z + 0.01))
				var result = space_state.intersect_ray(params)
				if result.is_empty() == true:
					pass
				else:
					var newVoxel = Voxel.new(Vector3(x,y,z),Vector3(delta_x,delta_y,delta_z),default_alpha,starting_temp)
					
					add_child(newVoxel)
			
		
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
