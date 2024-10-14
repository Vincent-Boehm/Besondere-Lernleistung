using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VoxelGrid : MonoBehaviour
{
    public Mesh mesh;
    public List<Vector3Int> gridPoints = new();
    public float halfSize = 0.1f;
    
    // Start is called before the first frame update
    void Start()
    {

    }

}
