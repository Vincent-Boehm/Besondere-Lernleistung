extends Node3D


@export var obj_file: Mesh

@export var delta_x: float
@export var delta_y: float
@export var delta_z: float

@export var size: float

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	for x in size:
		for y in size:
				for z in size:
					
		
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
