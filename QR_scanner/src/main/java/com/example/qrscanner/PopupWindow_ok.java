package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.ImageButton;
import android.widget.TextView;

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

            }
        });
        DisplayMetrics displayMetrics=new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(displayMetrics);
        int width=displayMetrics.widthPixels;
        int height=displayMetrics.heightPixels;
        getWindow().setLayout((int)(width*.6),(int)(height*.5));

    }
}
