package com.example.camerademo;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class ViewOcrActivity extends AppCompatActivity {

    Button btnSubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_ocr);
        btnSubmit = findViewById(R.id.btnSubmitOCR);

        btnSubmit.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v) {
                Toast.makeText(ViewOcrActivity.this, "Submission successful\nDecision will be given shortly", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(ViewOcrActivity.this, Dashboard.class);
                startActivity(intent);
                finish();
            }
        });
    }
}