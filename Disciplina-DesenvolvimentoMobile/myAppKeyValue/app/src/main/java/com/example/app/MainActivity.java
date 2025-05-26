package com.example.app;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    EditText editText;
    Button saveButton, goToSecondButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        editText = findViewById(R.id.editText);
        saveButton = findViewById(R.id.saveButton);
        goToSecondButton = findViewById(R.id.goToSecondButton);

        saveButton.setOnClickListener(v -> {

            EditText editText = findViewById(R.id.editText);
            String inputText = editText.getText().toString();

            SharedPreferences prefs = getSharedPreferences("MyPrefs", MODE_PRIVATE);
            SharedPreferences.Editor editor = prefs.edit();
            editor.putString("saved_text", inputText);
            editor.apply();

            Toast.makeText(MainActivity.this, "Texto salvo com sucesso!", Toast.LENGTH_SHORT).show();
        });

        goToSecondButton.setOnClickListener(v -> {
            Intent intent = new Intent(MainActivity.this, SecondActivity.class);
            startActivity(intent);
        });
    }
}
