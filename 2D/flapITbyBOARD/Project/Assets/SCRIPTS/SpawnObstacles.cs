using UnityEngine;
using System.Collections;

public class SpawnObstacles : MonoBehaviour {
	[SerializeField] private float _maxTime = 1.5f;
	[SerializeField] private float _heightRange = 0.45f;
	[SerializeField] private float _heightMin;
	[SerializeField] private GameObject _obstacle;
	[SerializeField] private GameObject _ground;
	[SerializeField] private float _startX = 25f;
	private float _timer;
	// Use this for initialization
	void Start () {
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
		GameObject Obstacle = Instantiate(_obstacle, spawnPos, Quaternion.identity) as GameObject;
		Destroy (Obstacle, 10f);
	}
}
