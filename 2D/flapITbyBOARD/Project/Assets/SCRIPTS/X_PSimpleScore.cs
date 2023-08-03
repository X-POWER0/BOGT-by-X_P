using UnityEngine;
using System.Collections;
using UnityEngine.Events;
using UnityEngine.EventSystems;
using UnityEngine.Serialization;
using UnityEngine.UI;

public class X_PSimpleScore : MonoBehaviour {
	public GameObject XscoreMaker;
	public GameObject XscoreTrigger;
	public GameObject XscoreDisplay;
	public GameObject XhighScoreDisplay;
	public float XscoreIncreasVal = 1f;
	public float XscoreDecreasVal = 1f;
	public float XscoreVal = 0f;
	public float XscoreValInitial = 0f;
	public float XhighScoreVal = 0f;
	public bool XscoreWrite;
	public bool XscoreRead;
	public string XscoreNumbersType = "000";
	public string XscoreGet;
	public bool XscoreON = true;
	public string PlPref_XHS_SvName = "XhighScore";
	public float PlPref_XHS_Loaded;
	public bool ResetPlPref = false;
	//- FROM function in another script

	public UnityEvent XscoreSet; 
	//- TO function in another script
	void Awake(){
		
		//XscoreMaker = GameObject.FindGameObjectWithTag("GameManager");
	}
	// Use this for initialization
	void Start () {
		//XscoreMaker = GameObject.FindGameObjectWithTag("GameManager");
		//if(PlayerPrefs.GetFloat (PlPref_XHS_SvName) > 0){
		PlPref_XHS_Loaded = PlayerPrefs.GetFloat (PlPref_XHS_SvName);
		//}
			XscoreVal = XscoreValInitial;
		if (PlPref_XHS_Loaded > 0){
			XhighScoreVal = PlPref_XHS_Loaded; 
		}
		else{
		XhighScoreVal = XscoreValInitial;
		}
		//XscoreDisplay.GetComponent<Text>().text = XscoreVal.ToString(XscoreNumbersType);
		XhighScoreDisplay.GetComponent<Text>().text = XhighScoreVal.ToString(XscoreNumbersType);
	}
	
	// Update is called once per frame
	void Update () {
		if(XscoreON){
			if(ResetPlPref)
			{
				//if(PlayerPrefs.GetFloat (PlPref_XHS_SvName) > 0){
					PlayerPrefs.DeleteKey (PlPref_XHS_SvName);
			//}
				ResetPlPref = false;}
		if(XscoreWrite){
			
				XscoreVal = XscoreValInitial + XscoreMaker.GetComponent<fITbB_main>().Timer;
			//XscoreDisplay.GetComponent<Text>().text = XscoreVal.ToString(XscoreNumbersType);
			//XscoreAdd();
			/*
			Collider2D Trig;
			XscoreMaker.GetComponent<Snake>().OnTriggerEnter2D(Trig);
			//XscoreMaker.GetComponent<AnotherScript>().MethodFromAnother(XscoreVal); in Another script sets in place of XscoreVal (float AnotherScriptVar)
			if(Trig == XscoreTrigger.GetComponent<Collider2D> ()){
				XscoreAdd();
			}
			*/
		}
		if(XscoreRead){
			//XscoreMaker.GetComponent<AnotherScript>().MethodFromAnother(XscoreVal); in Another script sets in place of XscoreVal (float AnotherScriptVar)
		}
		XhighScoreCal();
		}
	}
	private void FixedUpdate(){

	}
	public void XscoreAdd(){
		if(XscoreON){
		XscoreVal += XscoreIncreasVal;
		XscoreDisplay.GetComponent<Text>().text = XscoreVal.ToString(XscoreNumbersType);
	}
	}
	public void XscoreMinus(){
		if(XscoreON){
		XscoreVal -= XscoreDecreasVal;
		XscoreDisplay.GetComponent<Text>().text = XscoreVal.ToString(XscoreNumbersType);
	}
	}
	public void XscoreReset(){
		if(XscoreON){
		XscoreVal = XscoreValInitial;
		XscoreDisplay.GetComponent<Text>().text = XscoreVal.ToString(XscoreNumbersType);
		}
		}
	public void XhighScoreCal(){
		if(XscoreON){
		if (XscoreVal > XhighScoreVal){
			XhighScoreVal = XscoreVal;
				PlayerPrefs.SetFloat (PlPref_XHS_SvName, XhighScoreVal);
				PlayerPrefs.Save ();
		}
		XhighScoreDisplay.GetComponent<Text>().text = XhighScoreVal.ToString(XscoreNumbersType);
	}
	}
	public void XhighScoreReset(){
		if(XscoreON){
		XhighScoreVal = XscoreValInitial;
		XhighScoreDisplay.GetComponent<Text>().text = XhighScoreVal.ToString(XscoreNumbersType);
		}
	}
}
