using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class MoveObstacle : MonoBehaviour {
	[SerializeField] private float _speed = 0.65f; 
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
		transform.position += Vector3.left *_speed *Time.deltaTime;
	}
}
