package com.example.qrscanner;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

import com.google.zxing.Result;

import me.dm7.barcodescanner.zxing.ZXingScannerView;

public class ORscanner_code extends AppCompatActivity  implements ZXingScannerView.ResultHandler {
    ZXingScannerView scannerView;
    public static String qr_data=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        scannerView = new ZXingScannerView(this);
        setContentView(scannerView);
    }

    @Override
    public void handleResult(Result result) {
        qr_data=result.getText();
        startActivity(new Intent(getApplicationContext(),PopupWindow_ok.class));
        onBackPressed();
    }
    @Override
    protected void onPause() {
        scannerView.stopCamera();
        super.onPause();
    }

    @Override
    protected void onResume() {
        scannerView.setResultHandler(this);
        scannerView.startCamera();
        super.onResume();
    }

    @Override
    public void onBackPressed() {
        finish();
        startActivity(new Intent(getApplicationContext(),MainActivity.class));
        super.onBackPressed();
    }
}
