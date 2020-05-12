package com.example.qrscanner;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public class List_students extends AppCompatActivity {
    BottomNavigationView bottom_nav;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_list_students);

        bottom_nav=findViewById(R.id.bottom_nav_list);                       //for bottom nav bar in List acttivity
        bottom_nav.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.Webview_item:
                        startActivity(new Intent(getApplicationContext(), MainActivity.class));
                        break;
                    case R.id.List_item:
                        startActivity(new Intent(getApplicationContext(),List_students.class));
                        break;

                    case R.id.Scanner_item:
                        startActivity(new Intent(getApplicationContext(), ORscanner_code.class));
                        break;

                }
                return true;
            }
        });

    }

    @Override
    public void onBackPressed() {
        finishAffinity();
        startActivity(new Intent(getApplicationContext(),MainActivity.class));
        super.onBackPressed();
    }
}
