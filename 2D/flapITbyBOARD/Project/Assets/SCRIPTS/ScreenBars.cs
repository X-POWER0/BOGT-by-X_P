using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;


public class ScreenBars : MonoBehaviour {
	public enum ReferenceMode { DesignedAspectRatio, OriginalResolution};
	public ReferenceMode referenceMode;
	private Camera Cam;
	private Camera LetterBoxCam;
	public Color matteColor = new Color(0,0,0,1);
	public float x=757f;
	public float y=270f;
	public float width=757f;
	public float height=270f;
	public bool onAwake = true;
	public bool onUpdate = true;
	public bool CreatLetterBoxCam = true;
	public bool GetLetterBoxCam = false;
	public bool FindCam = false;
	public bool drawLetterBoXUI = false;
	public string MainCameraTag = "MainCamera";
	public string LetterBoxCamTag = "LetterBoxCam";
	public bool BarsOnTopLttrCam = false;
	public bool FindBars = false;
	public GameObject BarHightUp;
	public GameObject BarHightDown;
	public GameObject BarWidthL;
	public GameObject BarWidthR;
	
	public string BarHightUpTag = "BarHightUp";
	public string BarHightDownTag = "BarHightDown";
	public string BarWidthLTag = "BarWidthL";
	public string BarWidthRTag = "BarWidthR";

	public void Awake()
	{
		if(CreatLetterBoxCam){
			GetLetterBoxCam = false;
			AddLetterBoxCam();}
		else if(GetLetterBoxCam)
		   {
			CreatLetterBoxCam = false;
			FindLetterBoxCam();
		}
		if(!FindCam){
			Cam = GetComponent<Camera>();
		}
		if(FindCam){
		Cam = GameObject.FindGameObjectWithTag (MainCameraTag).GetComponent<Camera>();
		}
		if(BarsOnTopLttrCam){
		if(FindBars){
			BarHightUp = GameObject.FindGameObjectWithTag (BarHightUpTag);
			BarHightDown = GameObject.FindGameObjectWithTag (BarHightDownTag);
			//BarWidthL = GameObject.FindGameObjectWithTag (BarWidthLTag);
			//BarWidthR = GameObject.FindGameObjectWithTag (BarWidthRTag);
			}}
			if(onAwake){
			ChangeSize();
		}
	}

	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	public void Update () {
		if(onUpdate){
			ChangeSize();
		}
	}
	private void onValidate(){
		x = Mathf.Max (1, x);
		y = Mathf.Max (1, y);
		width = Mathf.Max (1, width);
		height = Mathf.Max (1, height);

	}
	private void AddLetterBoxCam()
	{
		///chouldn't be other cameras with depth -100
		LetterBoxCam = new GameObject().AddComponent<Camera>();
		LetterBoxCam.backgroundColor = matteColor;
		LetterBoxCam.cullingMask = 0;
		LetterBoxCam.depth = -100;
		LetterBoxCam.farClipPlane = 1;
		LetterBoxCam.useOcclusionCulling = false;
		LetterBoxCam.hdr = false;
		LetterBoxCam.clearFlags = CameraClearFlags.Color;
		LetterBoxCam.name = "LetterBoxCam";
	}
	private void FindLetterBoxCam(){
		LetterBoxCam = GameObject.FindGameObjectWithTag(LetterBoxCamTag).GetComponent<Camera>();
	}
	private void ChangeSize(){
		float targetRatio = x/y;
		if(referenceMode == ScreenBars.ReferenceMode.OriginalResolution ){
			targetRatio = width/height;
		}
		float windowaspect = (float)Screen.width / (float)Screen.height; 
		float scaleheight = windowaspect / targetRatio ; 

		if(scaleheight< 1.0f || drawLetterBoXUI)
		{
			Rect rect = Cam.rect;
			rect.width = 1.0f;
			rect.height = scaleheight;
			rect.x = 0;
			rect.y = (1.0f - scaleheight)/ 2.0f;
					Cam.rect = rect;
			if(BarsOnTopLttrCam){
				//BarHightUp.GetComponent<RectTransform>().SetInsetAndSizeFromParentEdge (RectTransform.Edge.Top,0,(1.0f - scaleheight)) ;
				//BarHightDown.GetComponent<RectTransform>().SetInsetAndSizeFromParentEdge (RectTransform.Edge.Bottom,0,(1.0f - scaleheight)) ;
				
				BarHightUp.GetComponent<RectTransform>().SetInsetAndSizeFromParentEdge (RectTransform.Edge.Top,0, 3 - (1.0f - scaleheight)/2.0f);
				BarHightDown.GetComponent<RectTransform>().SetInsetAndSizeFromParentEdge (RectTransform.Edge.Bottom,0, 3 - (1.0f - scaleheight)/2.0f);
				BarHightUp.GetComponent<RectTransform>().localScale = new Vector3(BarHightUp.GetComponent<RectTransform>().localScale.x, (1.0f - scaleheight)/2.0f, BarHightUp.GetComponent<RectTransform>().localScale.z) ;
				BarHightDown.GetComponent<RectTransform>().localScale = new Vector3(BarHightUp.GetComponent<RectTransform>().localScale.x, (1.0f - scaleheight)/2.0f, BarHightUp.GetComponent<RectTransform>().localScale.z);

			}
		}
		else{
			float scalewidth = 1.0f;
			Rect rect = Cam.rect;
			rect.width = scalewidth ;
			rect.height = 1.0f;
			rect.x = (1.0f - scalewidth)/ 2.0f;
			rect.y = 0;
			Cam.rect = rect;

		}
	}
}
