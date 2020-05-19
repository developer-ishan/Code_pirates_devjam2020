package com.example.qrscanner;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.material.bottomnavigation.BottomNavigationView;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;


public class List_students extends AppCompatActivity {
    BottomNavigationView bottom_nav;
    ProgressDialog progressDialog;
    private String result;
    InputStream inputStream;
    Context context=List_students.this;
    RecyclerView recyclerView;
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
                       // startActivity(new Intent(getApplicationContext(),List_students.class));
                        break;

                    case R.id.Scanner_item:
                        startActivity(new Intent(getApplicationContext(), ORscanner_code.class));
                        break;

                }
                return true;
            }
        });


        //setting up recyclerview

        recyclerView=findViewById(R.id.recyclerList);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        GetData getData=new GetData();
        getData.execute();

    }


    @Override
    public void onBackPressed() {
        finishAffinity();
        startActivity(new Intent(getApplicationContext(),MainActivity.class));
        super.onBackPressed();
    }





    public class GetData extends AsyncTask<String,Void,Void> {

        @Override
        protected Void doInBackground(String... strings) {
            String ConnectionUrl="http://localhost:8000/api/list";
            try {
                URL url=new URL(ConnectionUrl);
                HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
                httpURLConnection.setRequestMethod("POST");
                httpURLConnection.setDoInput(true);
                inputStream = new BufferedInputStream(httpURLConnection.getInputStream());
                result = convertStreamToString(inputStream);
                httpURLConnection.disconnect();
                Log.d("TAG",result+"");
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            } catch (ProtocolException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }

        private String convertStreamToString(InputStream inputStream) {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            StringBuilder sb = new StringBuilder("");
            String line;
            try {
                while ((line = bufferedReader.readLine()) != null) {
                    sb.append(line + "\n");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            try {
                inputStream.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return sb.toString();
        }

        @Override
        protected void onPreExecute() {
            progressDialog = ProgressDialog.show(context,"List is Loading...","Please wait...",false,false);;
            super.onPreExecute();
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            if(inputStream==null)
            {
                progressDialog.dismiss();
                Toast.makeText(context, "Server Not Responding", Toast.LENGTH_LONG).show();

                return ;
            }
            if(result!=null)
            {
                try {
                    JSONObject jsonObject=new JSONObject(result);
                    JSONArray jsonArray= jsonObject.getJSONArray("result");
                    java.util.List<Entrydata_getset> entrydataGetsets=new ArrayList<>();
                    for(int i=0;i<jsonArray.length();i++)
                    {
                       JSONObject Object=jsonArray.getJSONObject(i);

                       entrydataGetsets.add(new Entrydata_getset(Object.getString("id"),
                               Object.getString("name"),
                               Object.getString("regno"),
                               Object.getString("roomno"),
                               Object.getString("intime"),
                               Object.getString("outtime")));

                    }
                    recyclerView.setAdapter(new Adapter(entrydataGetsets));




                } catch (Exception e) {
                    e.printStackTrace();
                }


            }
            progressDialog.dismiss();


            super.onPostExecute(aVoid);
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            super.onProgressUpdate(values);
        }
    }




}
