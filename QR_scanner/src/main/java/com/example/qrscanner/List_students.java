package com.example.qrscanner;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.DownloadManager;
import android.content.Intent;
import android.os.Bundle;
import android.telecom.Call;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;



public class List_students extends AppCompatActivity {
    BottomNavigationView bottom_nav;
    public static TextView data;
    ListView listView;
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
        listView=findViewById(R.id.list_main);
        fetchingData();
    }

    private void fetchingData() {

        String myURL = " your web URl";
        JsonArrayRequest jsonArrayRequest = new JsonArrayRequest(myURL, new Response.Listener<JSONArray>() {
            @Override
            public void onResponse(JSONArray response) {
                final String[] student_detail = new String[response.length()];
                for (int i = 0; i < response.length(); i++) {
                    try {

                        JSONObject jsonObject = (JSONObject) response.get(i);
                        student_detail[i] = jsonObject.getString("Student_details");

                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
                listView.setAdapter(new ArrayAdapter(getApplicationContext(), R.layout.mylistview, R.id.textView_forlist, student_detail));
                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Intent intent = new Intent(List_students.this, Details.class);
                        intent.putExtra("Student_details", student_detail[position]);
                        startActivity(intent);

                    }
                });
            }
        }
                , new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                VolleyLog.d("Volley Log", error);
            }
        }
        );

        //.AppController.getInstance().addToRequestQueue(jsonArrayRequest);
        Toast.makeText(getApplicationContext(), "Data Loaded Successfully!", Toast.LENGTH_SHORT).show();

    }

    @Override
    public void onBackPressed() {
        finishAffinity();
        startActivity(new Intent(getApplicationContext(),MainActivity.class));
        super.onBackPressed();
    }
}
