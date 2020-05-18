package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class Landing extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_landing);
        final ImageView image=findViewById(R.id.img_rotate);
        final Animation animation= AnimationUtils.loadAnimation(getApplicationContext(),R.anim.scale_anim);
        image.setAnimation(animation);


        CountDownTimer timer =new CountDownTimer(4000,1000) {
            @Override
            public void onTick(long millisUntilFinished) {

            }

            @Override
            public void onFinish() {
               Intent i=new Intent(getApplicationContext(),MainActivity.class);
               startActivity(i);
            }
        }.start();


    }
}
