package com.example.qrscanner;

import android.app.ProgressDialog;
import android.content.Context;
import android.os.AsyncTask;
import android.util.Log;
import android.widget.ProgressBar;
import android.widget.Toast;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;
import java.net.URLEncoder;

    public class Senddata extends AsyncTask<String ,Void,Void> {

        private String qr_data=ORscanner_code.qr_data;
        String[] getting_reg_no = qr_data.split(";");
        String reg_url = getting_reg_no[0];
        private String result;

        @Override
        protected Void doInBackground(String... strings) {
            String url_true = "http://127.0.0.1:8000/api/tick-status/"+reg_url;
            Log.d("url",url_true);
            try {
                URL url = new URL(url_true+"/true");
                Log.d("url",url.toString());
                HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
                httpURLConnection.setRequestMethod("GET");
                httpURLConnection.setDoInput(true);
                OutputStream out = httpURLConnection.getOutputStream();
                BufferedWriter bufferedWriter;
                bufferedWriter = new BufferedWriter(new OutputStreamWriter(out, "UTF-8"));
                String data = URLEncoder.encode(qr_data, "UTF-8");
                bufferedWriter.write(data);
                bufferedWriter.flush();
                bufferedWriter.close();
                InputStream inputStream = new BufferedInputStream(httpURLConnection.getInputStream());
                result = convertStreamToString(inputStream);
                httpURLConnection.disconnect();
                Log.d("TAG", result + "");
                Log.d("Doin background","working");

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
                    Log.d("convertStreamToString","working");
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
            Log.d("onPreExecute","working");
            super.onPreExecute();
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            Log.d("onPostExecute","working");
            super.onPostExecute(aVoid);
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            Log.d("onProgressupdate","working");
            super.onProgressUpdate(values);

        }
    }


