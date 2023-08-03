using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class ImgLoop : MonoBehaviour {
	
	[SerializeField] private float _speed = 1f;
	[SerializeField] private float _width = 6f;

	private SpriteRenderer _spriteRenderer;
	//Unity5> private Vector2 _startSize;
	private Vector3 _startSize;
	float PixelIsPerUnit;
	Vector3 _startPos;
	// Use this for initialization
	void Start () {
	
		/* 	//Unity5>
		_spriteRenderer = GetComponent<SpriteRenderer>();
		_startSize = new Vector2(_spriteRenderer.size.x, _spriteRenderer.size.y);
	*/
		_spriteRenderer = GetComponent<SpriteRenderer>();
		_startSize = new Vector2(_spriteRenderer.sprite.border.x, _spriteRenderer.sprite.border.y);
		PixelIsPerUnit = _spriteRenderer.sprite.pixelsPerUnit;
		_startPos = _spriteRenderer.transform.position;
	}
	
	// Update is called once per frame
	void Update () {
		//unity5> _spriteRenderer.size = new Vector2(_spriteRenderer.size.x + _speed * Time.deltaTime, _spriteRenderer.size.y)
		_spriteRenderer.transform.position = new Vector3(_spriteRenderer.transform.position.x + _speed * Time.deltaTime, _startPos.y, _startPos.z);
		//unity5> if(_spriteRenderer.size.x > _width)(_spriteRenderer.size = _startSize;}
		if(_spriteRenderer.transform.position.x > _startPos.x + _spriteRenderer.sprite.bounds.size.x * PixelIsPerUnit -0.5f ){
			_spriteRenderer.transform.position = _startPos;
		}
	}
}
