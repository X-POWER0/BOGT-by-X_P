using UnityEngine;
using System.Collections;

using System.Collections.Generic;

public class SpawnObstacles2 : MonoBehaviour {
	[SerializeField] private float _maxTime = 1.5f;
	[SerializeField] private float _heightRange = 0.45f;
	[SerializeField] private float _heightMin;
	
	[SerializeField] private GameObject _obstacle1;
	
	[SerializeField] private GameObject _obstacle2;
	[SerializeField] private GameObject _obstacle3;
	public List<GameObject> _obstacleS;
	[SerializeField] private GameObject _ground;
	[SerializeField] private float _startX = 25f;
	int ObstacleRandomNumber;
	public int ObstacleNumber;
	private float _timer;
	// Use this for initialization
	void onEnable(){
	}
		void Start () {

		_obstacleS.Add (_obstacle1);
		_obstacleS.Add (_obstacle2);
		_obstacleS.Add (_obstacle3);
		
		ObstacleRandomNumber = Random.Range(0,2);
		ObstacleNumber = ObstacleRandomNumber;
		_heightMin = _ground.transform.position.x + _ground.GetComponent<BoxCollider2D>().size.y;
		SpawnObstacle();
	
	}
	
	// Update is called once per frame
	void Update () {
	if (_timer > _maxTime)
		{
			SpawnObstacle();
			_timer = 0;
		}
		_timer += Time.deltaTime;
	}
	public void SpawnObstacle(){
		Vector3 spawnPos = transform.position + new Vector3(_startX, Random.Range (_heightMin, _heightRange));
		GameObject Obstacle = Instantiate(_obstacleS[ObstacleNumber], spawnPos, Quaternion.identity) as GameObject;
		Destroy (Obstacle, 10f);
	}
}
