using UnityEngine;
using System.Collections;

public class PlaySoundX : MonoBehaviour {
	public AudioClip collide1;
	public AudioClip collide2;
	public AudioClip collide3;
	public AudioClip flapped;
	public AudioClip nxtlvl;
	public AudioSource AudioPlayer;

	// Use this for initialization
	void Start () {
		AudioPlayer = GetComponent<AudioSource>();
	}
	
	// Update is called once per frame
	void Update () {
	
	}
	
	public void PlayCollide(){
		if(AudioPlayer.clip != collide1){
			AudioPlayer.PlayOneShot(collide1, 0.1f);
		}
		else if(AudioPlayer.clip != collide2){
			AudioPlayer.PlayOneShot(collide2, 0.1f);
		}
		else if(AudioPlayer.clip != collide3)
			AudioPlayer.PlayOneShot(collide3, 0.1f);}

	public void PlayFlapped(){
		if(AudioPlayer.clip != flapped){
		AudioPlayer.PlayOneShot(flapped, 0.1f);}
	}
		
	public void PlayNxtlvl(){
		
		if(AudioPlayer.clip != nxtlvl){
		AudioPlayer.PlayOneShot(nxtlvl, 0.6f);
		}}
}
