using UnityEngine;
using System.Collections;
using System.Collections.Generic;


public class ITfly : MonoBehaviour {
	[SerializeField] private float _velocity = 1.5f;
	[SerializeField] private float _velocityFly = 3.5f;
	[SerializeField] private float _rotationSpeed = 10f;
	[SerializeField] private string BoardTag = "Board";
	[SerializeField] private string NextlvlTag = "Nextlvl";
	GameObject GameManager;
	[SerializeField] private Animator ITanimator;
	[SerializeField] private string _animName = "flap";
	private Rigidbody2D _rb;
	GameObject MainAudioSource;
	AudioSource flapingAudioSource;
	AudioSource moveAudioSource;
	AudioClip moveAudioLeft;
	AudioClip moveAudioRight;
	// Use this for initialization
	void Start () {

		_rb = GetComponent<Rigidbody2D>();
		GameManager = GameObject.FindGameObjectWithTag("GameManager");
		flapingAudioSource = GameManager.transform.Find ("AudioFlapping").GetComponent<AudioSource>();
		moveAudioSource = GameManager.transform.Find ("AudioMove").GetComponent<AudioSource>();
		
		moveAudioLeft = GameManager.transform.Find ("AudioMove").GetComponent<PlaySoundX>().collide1;
		moveAudioRight = GameManager.transform.Find ("AudioMove").GetComponent<PlaySoundX>().collide2;
		MainAudioSource = GameManager.transform.Find ("AudioCollide").gameObject;

	}
	
	// Update is called once per frame
	void Update () {
		// in new Unity using UnityEngine.InputSystem if(Mouse.current.leftButton.wasPressedThisFrame)
		if(Input.GetMouseButton (1) || Input.GetButton("Jump")){
			ITanimator.SetBool (_animName, true);
			_rb.velocity = Vector2.up * _velocityFly;
			PlayFlapping();
		}
		if(Input.GetMouseButtonUp (1) || Input.GetButtonUp("Jump")){
			ITanimator.SetBool (_animName, false);
		}
		if(Input.GetAxisRaw("Horizontal") > 0 ){
			_rb.velocity = new Vector2(1 * _velocity, _rb.velocity.y);
			PlayMoveRight();
		}
		if(Input.GetAxisRaw("Horizontal") < 0 ){
			_rb.velocity = new Vector2(-1 * _velocity, _rb.velocity.y);
			PlayMoveLeft();
		}
		//MobControls
		
	//	Debug.Log(GameManager.GetComponent<fITbB_main>().MbControlJumpbtnPressed);
		if(GameManager.GetComponent<fITbB_main>().MbControlJumpbtnPressed){
			ITanimator.SetBool (_animName, true);
			_rb.velocity = Vector2.up * _velocityFly;
			PlayFlapping();
		}
//	if(!GameManager.GetComponent<fITbB_main>().MbControlJumpbtnPressed){
//			ITanimator.SetBool (_animName, false);}
		
		if(GameManager.GetComponent<fITbB_main>().MbControlRightbtnPressed ){
			_rb.velocity = new Vector2(1 * _velocity, _rb.velocity.y);
			PlayMoveRight();

		}
		if(GameManager.GetComponent<fITbB_main>().MbControlLeftbtnPressed){
			_rb.velocity = new Vector2(-1 * _velocity, _rb.velocity.y);
			PlayMoveLeft();
		}

	}

	private void FixedUpdate(){
		transform.rotation = Quaternion.Euler (0, 0, _rb.velocity.y * _rotationSpeed);
	}

	private void OnCollisionEnter2D(Collision2D collision){
		
		MainAudioSource.GetComponent<PlaySoundX>().PlayCollide();
		//Debug.Log (collision.gameObject);
		if(collision.gameObject.tag == BoardTag){
		//	Debug.Log ("asda");
			MainAudioSource.GetComponent<PlaySoundX>().PlayFlapped();
			fITbB_main.instance.GameOver();

		}
	}
	
	private void OnTriggerEnter2D(Collider2D other){
		
		Debug.Log (other.tag);
		if(other.tag == NextlvlTag){
			
			MainAudioSource.GetComponent<PlaySoundX>().PlayNxtlvl();
			Debug.Log ("asda");
			fITbB_main.instance.NextLvl();
		}
	}
	public void NoAnimFly(){

		ITanimator.SetBool (_animName, false);
	}
	public void PlayFlapping(){
		if(!flapingAudioSource.isPlaying){
			flapingAudioSource.Play ();
			Debug.Log ("Flap");
			StartCoroutine (LikeInvoke(flapingAudioSource, 0.4f));
		}
	}
	public void PlayMoveLeft(){
		if(!moveAudioSource.isPlaying || moveAudioSource.clip != moveAudioLeft){
			Debug.Log ("Left");
			moveAudioSource.clip = moveAudioLeft;
			moveAudioSource.Play ();
			StartCoroutine (LikeInvoke(moveAudioSource, 0.5f));
		}
	}
	
	public void PlayMoveRight(){
		if(!moveAudioSource.isPlaying || moveAudioSource.clip != moveAudioRight){
			Debug.Log ("Right");
			moveAudioSource.clip = moveAudioRight;
			moveAudioSource.Play ();
			StartCoroutine (LikeInvoke(moveAudioSource, 0.5f));
		}
	}
	private void StopSound(AudioSource AudioPlayer){
		AudioPlayer.Stop ();
	}
			IEnumerator LikeInvoke(AudioSource AudioPlayer, float delayTime){
		yield return new WaitForSeconds(delayTime);		
		StopSound(AudioPlayer);
			}
}
