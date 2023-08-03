using UnityEngine;
using System.Collections;

public class RandomColor : MonoBehaviour {

	// Use this for initialization
	void Start () {
		this.GetComponent<SpriteRenderer>().color = new Color( Random.Range (0f,0.4f),Random.Range (0f,0.4f),Random.Range (0f,0.4f),1f);
	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
