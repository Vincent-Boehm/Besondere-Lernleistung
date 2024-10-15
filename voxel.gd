class_name Voxel
extends Node3D

@export var alpha:float
@export var temp:float

func _init(position:Vector3 = Vector3(0,0,0),size:Vector3 = Vector3(0,0,0),_alpha:float = 0,_temp:float = 0) -> void:
	global_position = position
	
	alpha = _alpha
	temp = _temp
	
	var box = CSGBox3D.new()
	box.size = size
	
	add_child(box)
	print("I am a newly created voxel")
	pass
func _ready() -> void:
	pass
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
