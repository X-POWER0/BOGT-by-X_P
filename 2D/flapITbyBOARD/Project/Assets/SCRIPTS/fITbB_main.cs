using UnityEngine;
using UnityEngine.UI;
using System.Collections;
//in Unity 5> using UnityEngine.ScenManagement;

public class fITbB_main : MonoBehaviour {
	public static fITbB_main instance;
	[SerializeField]private GameObject _gameOverPanel;
	[SerializeField]private GameObject _gamePausePanel;
	[SerializeField]private GameObject _iT;

	[HideInInspector]public float Timer;
	[SerializeField] private GameObject TimerText;
	[SerializeField] private int indexLevel1 = 1;
	[SerializeField] private int indexLevel2 = 2;
	public bool DontDestrON = false;
	float buttonPressTime = 0.1f;
	float frozenTime;
	public bool playing = true;
	public bool MbControlXbtnPressed = false;
	public bool MbControlJumpbtnPressed = false;
	public bool MbControlUPbtnPressed = false;
	public bool MbControlDownbtnPressed = false;
	public bool MbControlLeftbtnPressed = false;
	public bool MbControlRightbtnPressed = false;



	private void Awake(){
		if(DontDestrON){
		DontDestroyOnLoad(this.gameObject);
		}
			if(instance == null){
			instance = this;
		}
		Time.timeScale = 1f;
	}
	// Use this for initialization

	void Start () {
	//	_gameOverPanel = GameObject.FindWithTag("GameOver");
	//	_gamePausePanel = GameObject.FindWithTag("Pause");

		_gameOverPanel = GameObject.FindGameObjectWithTag("GameOver").transform.Find("GameOver").gameObject;
		
		_gamePausePanel = GameObject.FindGameObjectWithTag("Pause").transform.Find("Pause").gameObject;
		TimerText.GetComponent<Text>().text = Timer.ToString("000");
	}
	
	// Update is called once per frame
	void Update () {
		if(playing){
			Timer += 1 * Time.deltaTime;
			TimerText.GetComponent<Text>().text = Timer.ToString("000");
			if(Input.GetButtonDown("Cancel") || Input.GetKeyDown(KeyCode.Escape)  || MbControlXbtnPressed ){
				PauseGame();
				buttonPressTime = Time.time + Time.deltaTime*0.1f;
				frozenTime = Time.time;
				Debug.Log (buttonPressTime);
			}
		}
		if(_gamePausePanel.activeInHierarchy){
			if(buttonPressTime < frozenTime){
				frozenTime += 1f;}
			//Debug.Log (buttonPressTime);
			//Debug.Log (frozenTime);
			//Debug.Log (buttonPressTime < frozenTime);
			if(Input.GetButtonDown("Cancel") || Input.GetKeyDown(KeyCode.Escape) || MbControlXbtnPressed ){
				frozenTime += 0.001f;
			//	Debug.Log (buttonPressTime);
				if(buttonPressTime < frozenTime){
					PlayGame();
				}
			}
			if(Input.GetButtonDown("Submit") || Input.GetKeyDown(KeyCode.Return) ){
				Application.Quit();
			}
		}
		if(_gameOverPanel.activeInHierarchy){
			if(Input.GetButtonDown("Submit") || Input.GetKeyDown(KeyCode.Return) ){
				RestartGame();
			}
			if(Input.GetButtonDown("Cancel") || Input.GetKeyDown(KeyCode.Escape) ){
				Application.Quit();
			}
		}
	}
	public void GameOver(){
		playing = false;
		
		_gameOverPanel = GameObject.FindGameObjectWithTag("GameOver").transform.Find("GameOver").gameObject;
		_gameOverPanel.SetActive(true);
		Time.timeScale = 0f;
	}
	public void PauseGame(){
		playing = false;
		//FindObjectsOfTypeAll();
		_gamePausePanel = GameObject.FindGameObjectWithTag("Pause").transform.Find("Pause").gameObject;
		_gamePausePanel.SetActive(true);
		Time.timeScale = 0f;
	}
	public void PlayGame(){
		playing = true;
		_gamePausePanel.SetActive(false);
		Time.timeScale = 1f;
	}

	public void RestartGame(){
		_gameOverPanel.SetActive(false);
		//in Unity 5> ScenManager.LoadScene(ScenManager.GetActiveScene().buildIndex);
		Application.LoadLevel(indexLevel1);
		
		playing = true;
		Timer = 0f;
		Time.timeScale = 1f;
	}
	public void StartGame(){

		//in Unity 5> ScenManager.LoadScene(ScenManager.GetActiveScene().buildIndex);
		Application.LoadLevel(indexLevel1);
		
		playing = true;
	}
	
	public void NextLvl(){
		
		playing = false;
		Time.timeScale = 0f;
		//in Unity 5> ScenManager.LoadScene(ScenManager.GetActiveScene().buildIndex);
		if(	Application.loadedLevel == indexLevel1){
			Application.LoadLevel(indexLevel2);
			
			playing = true;
			
			Time.timeScale = 1f;

		}
		else if(	Application.loadedLevel == indexLevel2){
			Application.LoadLevel(indexLevel1);
			
			playing = true;
			
			Time.timeScale = 1f;
		}
	}
	public void SoundOFFX(){
		AudioListener.pause = !AudioListener.pause;
	}
	public void QuitGame(){
		//in Unity 5> ScenManager.LoadScene(ScenManager.GetActiveScene().buildIndex);
		Application.Quit();
	}
	
	public void MoreLink(){
		//in Unity 5> ScenManager.LoadScene(ScenManager.GetActiveScene().buildIndex);
		Application.OpenURL("https://x-pmods.itch.io/bogt-by-x-p");
	}
	//MobControls
	public void pressX(){
		MbControlXbtnPressed = true;}
	public void pressRight(){
		MbControlRightbtnPressed = true;}
	public void pressLeft(){
		MbControlLeftbtnPressed = true;}
	public void pressDown(){
		MbControlDownbtnPressed = true;}
	public void pressUp(){
		MbControlUPbtnPressed = true;}

	public void pressJump(){
		MbControlJumpbtnPressed = true;}
	
	public void pressXUP(){
		MbControlXbtnPressed = false;}
	public void pressRightUP(){
		MbControlRightbtnPressed = false;}
	public void pressLeftUP(){
		MbControlLeftbtnPressed = false;}
	public void pressDownUP(){
		MbControlDownbtnPressed = false;}
	public void pressUpUP(){
		MbControlUPbtnPressed = false;}
	
	public void pressJumpUP(){
		MbControlJumpbtnPressed = false;}
	public void AnimOFFonUIbtn(){
		_iT = GameObject.FindGameObjectWithTag("Player");
		_iT.GetComponent<ITfly>().NoAnimFly();
	}
}
