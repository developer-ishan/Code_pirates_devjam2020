package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.util.DisplayMetrics;
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

import java.util.HashMap;
import java.util.Map;

import pl.droidsonroids.gif.GifImageView;

public class PopupWindow_ok extends AppCompatActivity {
    private static TextView name_,regno_,roomno_;
    ImageButton imbtn_confirm;
    GifImageView gifImageView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_popup_window_ok);


        name_=findViewById(R.id.tv_display_name);
        regno_=findViewById(R.id.tv_display_regno);
        roomno_=findViewById(R.id.tv_display_room);

        //setting data in the textviews
        String[] Spliting_data=ORscanner_code.qr_data.split(";");
        name_.setText(Spliting_data[1]);
        regno_.setText(Spliting_data[0]);
        roomno_.setText(Spliting_data[2]);


        imbtn_confirm=findViewById(R.id.imageButton_confirm);
        gifImageView=findViewById(R.id.gif_success);
        final LinearLayout layout=findViewById(R.id.pop_layout_li);


        imbtn_confirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
             Senddata sendData=new Senddata();
             sendData.execute();

             gifImageView.setVisibility(View.VISIBLE);
             layout.setVisibility(View.INVISIBLE);

                CountDownTimer timer=new CountDownTimer(1200,800) {
                    @Override
                    public void onTick(long millisUntilFinished) {

                    }

                    @Override
                    public void onFinish() {
                        startActivity(new Intent(getApplicationContext(),MainActivity.class));
                        Toast.makeText(getApplicationContext(),"Added to list",Toast.LENGTH_SHORT).show();
                    }
                }.start();

             /*       String Url = "https://swapi.dev/api/planets/3/";
                    StringRequest stringRequest = new StringRequest(Request.Method.POST, Url, new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                        }
                    }, new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {

                        }
                    }
                    ) {
                        protected Map<String, String> getParams() {
                            Map<String, String> parr = new HashMap<String, String>();
                            parr.put("data",ORscanner_code.qr_data );
                            return parr;
                        }

                    };
                    AppController.getInstance().addToRequestQueue(stringRequest);

                    Toast.makeText(getApplicationContext(), "uploaded Successfully!", Toast.LENGTH_LONG).show();
                }*/

        }});


            }

        }