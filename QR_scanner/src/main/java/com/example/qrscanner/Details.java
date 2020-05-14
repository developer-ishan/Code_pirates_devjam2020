package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class Details extends AppCompatActivity {
        TextView details;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);
        details = (TextView) findViewById(R.id.textView_details_student);
        String _Student_details = getIntent().getStringExtra("Student_details");
        details.setText(_Student_details);
    }
}
