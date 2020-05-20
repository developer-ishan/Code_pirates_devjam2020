package com.example.qrscanner;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.squareup.picasso.Picasso;

import java.sql.Array;
import java.sql.Time;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Calendar;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

import pl.droidsonroids.gif.GifImageView;

public class PopupWindow_ok extends AppCompatActivity {
    private static TextView name_,regno_,roomno_;
    ImageButton imbtn_confirm;
    ImageView image_user;
    GifImageView gifImageView;
    private  String[] Spliting_data=ORscanner_code.qr_data.split(";");
    private String time;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_popup_window_ok);

         image_user=findViewById(R.id.imgv_user);
        name_=findViewById(R.id.tv_display_name);
        regno_=findViewById(R.id.tv_display_regno);
        roomno_=findViewById(R.id.tv_display_room);

        //setting data in the textviews

        name_.setText(Spliting_data[1]);
        regno_.setText(Spliting_data[0]);
        roomno_.setText(Spliting_data[2]);
        String URL_image=Spliting_data[3];

        long date=System.currentTimeMillis();
        SimpleDateFormat format=new SimpleDateFormat("EEE dd MM,HH:mm a");
        time= format.format(date);

        //adding user image
        Picasso.get()
                .load(URL_image)
                .error(R.drawable.ic_person_orange_24dp)
                .into(image_user);


        imbtn_confirm=findViewById(R.id.imageButton_confirm);
        gifImageView=findViewById(R.id.gif_success);
        final LinearLayout layout=findViewById(R.id.pop_layout_li);


        imbtn_confirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //Senddata sendData=new Senddata();
                // sendData.execute();

             gifImageView.setVisibility(View.VISIBLE);
             layout.setVisibility(View.INVISIBLE);

                CountDownTimer timer=new CountDownTimer(2000,1000) {
                    @Override
                    public void onTick(long millisUntilFinished) {

                    }

                    @Override
                    public void onFinish() {
                        startActivity(new Intent(getApplicationContext(),List_students.class));
                    }
                }.start();

                senddata();



        }});


            }
            private void senddata(){
                final String[] in_time = new String[1];
                DatabaseReference db_check=FirebaseDatabase.getInstance().getReference();
                db_check.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        if(dataSnapshot.child("Entry_data").child("ENTRY_SVBH").child(Spliting_data[0]).exists()) {



                            Map<String, Object> user_info = new HashMap<>();

                                user_info.put("name", Spliting_data[1]);
                                user_info.put("reg_no", "Reg no. :" + Spliting_data[0]);
                                user_info.put("room_no", "Room no. :" + Spliting_data[2]);
                                user_info.put("in_time", "IN :" + time);
                                Log.d("intime__________", "_________________________working __________________");

                            DatabaseReference database = FirebaseDatabase.getInstance().getReference().child("Entry_data").child("ENTRY_SVBH").child(Spliting_data[0]);
                            database.updateChildren(user_info).addOnCompleteListener(new OnCompleteListener<Void>() {
                                @Override
                                public void onComplete(@NonNull Task<Void> task) {
                                    if (task.isSuccessful()) {
                                        Toast.makeText(getApplicationContext(), "data  added", Toast.LENGTH_SHORT).show();
                                    } else {
                                        String error = task.getException().getMessage();
                                        Toast.makeText(getApplicationContext(), error, Toast.LENGTH_SHORT).show();
                                    }

                                }
                            });
                        }
                        else {
                            Map<String, Object> user_info = new HashMap<>();
                            user_info.put("name", Spliting_data[1]);
                            user_info.put("reg_no", "Reg no. :" + Spliting_data[0]);
                            user_info.put("room_no", "Room no. :" + Spliting_data[2]);
                            user_info.put("in_time", "IN :");
                            user_info.put("out_time", "OUT :" + time);
						    Log.d("out_time__________", "_________________________working __________________");

                            DatabaseReference database = FirebaseDatabase.getInstance().getReference().child("Entry_data").child("ENTRY_SVBH").child(Spliting_data[0]);
                            database.updateChildren(user_info).addOnCompleteListener(new OnCompleteListener<Void>() {
                                @Override
                                public void onComplete(@NonNull Task<Void> task) {
                                    if (task.isSuccessful()) {
                                        Toast.makeText(getApplicationContext(), "data  added", Toast.LENGTH_SHORT).show();
                                    } else {
                                        String error = task.getException().getMessage();
                                        Toast.makeText(getApplicationContext(), error, Toast.LENGTH_SHORT).show();
                                    }

                                }
                            });
                        }
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {
                    }
                });






            }

        }