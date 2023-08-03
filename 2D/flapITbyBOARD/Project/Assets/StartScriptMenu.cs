using UnityEngine;
using System.Collections;

public class StartScriptMenu : MonoBehaviour {
	
	[SerializeField] private int indexLevel1 = 1;
	
	[SerializeField]private GameObject _gameManager;
	[SerializeField]private GameObject _mobControl;
	// Use this for initialization
	void Start () {
	
	}
	
	// Update is called once per frame
	void Update () {
			if(Input.GetButtonDown("Submit") || Input.GetKeyDown(KeyCode.Return) ){
			_gameManager.GetComponent<fITbB_main>().StartGame();
			this.gameObject.SetActive (false);
			}
			if(Input.GetButtonDown("Cancel") || Input.GetKeyDown(KeyCode.Escape) ){
				Application.Quit();
			}
	
}
	public void MobControlON(){
	if(_mobControl.activeInHierarchy){
			_mobControl.SetActive(false);}
		
		else if(!_mobControl.activeInHierarchy){
			_mobControl.SetActive(true);}
	}
}