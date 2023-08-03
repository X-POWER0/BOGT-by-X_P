using UnityEngine;
using System.Collections;

public class GETfreeAspectRatio : MonoBehaviour {
	public Camera Cam;

	// Use this for initialization
	void Start () {
		Debug.Log (Cam.aspect);
			
			Debug.Log (Cam.pixelHeight + " " + Cam.pixelWidth  );


	}
	
	// Update is called once per frame
	void Update () {
	
	}
}
