package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;

import java.util.HashMap;
import java.util.Map;

public class PopupWindow_ok extends AppCompatActivity {
    public static TextView qr_text;
    ImageButton imbtn_confirm;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_popup_window_ok);


        qr_text=findViewById(R.id.textView_qr_data);
        qr_text.setText(ORscanner_code.qr_data);
        imbtn_confirm=findViewById(R.id.imageButton_confirm);
        imbtn_confirm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    String Url = "url";
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
                }

        });
        DisplayMetrics displayMetrics=new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        int width=displayMetrics.widthPixels;
        int height=displayMetrics.heightPixels;
        getWindow().setLayout((int)(width*.6),(int)(height*.5));

    }
}
