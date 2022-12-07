@file:Suppress("CanBeVal")

package com.example.my_app

import android.icu.number.NumberFormatter.with
import android.os.Build
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.text.Editable
//import android.text.TextWatcher
import android.util.Log
import android.view.View
import android.widget.*
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.core.os.postDelayed
import androidx.core.widget.doAfterTextChanged
import com.chaquo.python.PyObject
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import com.google.android.material.textfield.TextInputEditText
import com.squareup.picasso.Callback
import com.squareup.picasso.Picasso
import java.lang.Exception
import java.util.*
import kotlin.collections.ArrayList
import kotlin.concurrent.schedule

//import io.reactivex.rxjava3.android.schedulers.AndroidSchedulers
//import io.reactivex.rxjava3.subjects.PublishSubject
//import kotlinx.coroutines.Dispatchers
//import kotlinx.coroutines.flow.*
//import java.util.*
//import java.util.concurrent.TimeUnit
//import kotlin.concurrent.schedule


class MainActivity : AppCompatActivity() {
    @RequiresApi(Build.VERSION_CODES.Q)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        supportActionBar?.hide()
        initPython()

        val imageview = findViewById<ImageView>(R.id.thumbnail)
        val textViewLyrics = findViewById<TextView>(R.id.textViewlyrics)
        val textViewTitle = findViewById<TextView>(R.id.textViewTitle)
        val searchBar = findViewById<AutoCompleteTextView>(R.id.Search_bar)
        val progressBar = findViewById<ProgressBar>(R.id.progressBar)
        progressBar.bringToFront()
        textViewTitle.bringToFront()


        var suggestions = ArrayList<String>()
        var arrayAdapter = ArrayAdapter<String>(this@MainActivity, android.R.layout.select_dialog_item, suggestions)
        searchBar.setAdapter(arrayAdapter)
        var timer = Timer()
        var length = 0
        var handler = Handler(Looper.getMainLooper())


        searchBar.setOnItemClickListener { parent, view, position, id ->
            //searchBar.clearFocus()
            progressBar.visibility = View.VISIBLE
            val selectedItem = parent.getItemAtPosition(position).toString()


            //val requestReturned = getRequest(selectedItem)

            var requestReturned = getRequest(selectedItem.toString())
            //val end = System.nanoTime()
            if (requestReturned.joinToString("")=="Erreur"){

            }
            else {

                val lyrics = requestReturned[0].toString()
                val songName = requestReturned[1].toString()
                val singer = requestReturned[2].toString()
                var cover = requestReturned[3].toString()
                val infos = "${songName} By ${singer}"







                //progressBar.visibility = View.GONE










                Picasso
                    .get()
                    .load(cover)
                    .into(imageview, object : Callback {
                        override fun onSuccess() {
                            textViewLyrics.text = lyrics //TextViewLyrics.text = requestReturned.toString()
                            textViewTitle.text = infos
                            progressBar.visibility = View.GONE
                            searchBar.clearFocus()

                        }

                        override fun onError(e: Exception?) {
                            TODO("Not yet implemented")
                        }

                    })


                //TextViewLyrics.text = requestReturned.toString()

                //textViewLyrics.text = lyrics //TextViewLyrics.text = requestReturned.toString()
                //textViewTitle.text = infos



                //handler.postDelayed({
                //    progressBar.visibility = View.GONE
                //}, 1000)


            }
        }



        searchBar.doAfterTextChanged { text ->
            timer.cancel() // cancel any previous delay
            timer = Timer() // schedule a new one
            timer.schedule(350L) {
                searchBar.handler.post {
                    //suggestions.clear()


                    if (text.toString().length==0){
                    }
                    //else if((text.toString().length)-length<=3){

                    //}
                    else{
                        //val begin = System.nanoTime()
                        //var autoCompleteReturned = getRequestAutoComplete(text.toString())

                        var foo = Fooo(text.toString())
                        var thread = Thread(foo)
                        thread.start()
                        thread.join()
                        var autoCompleteReturned = foo.okk
                        //val end = System.nanoTime()
                        if (autoCompleteReturned.joinToString("")=="Erreur"){
                        }else{
                            val song1_song = autoCompleteReturned[0].toString()
                            val song1_singer = autoCompleteReturned[1].toString()

                            val song2_song = autoCompleteReturned[2].toString()
                            val song2_singer = autoCompleteReturned[3].toString()

                            val song3_song = autoCompleteReturned[4].toString()
                            val song3_singer = autoCompleteReturned[5].toString()

                            Log.i("Liverpool", "$song1_song ($song1_singer)")
                            Log.i("Liverpool", "$song2_song ($song2_singer)")
                            Log.i("Liverpool", "$song3_song ($song3_singer)")

                            suggestions.add("$song1_song ($song1_singer)")
                            suggestions.add("$song2_song ($song2_singer)")
                            suggestions.add("$song3_song ($song3_singer)")



                            //suggestions.add("$song1_song ($song1_singer)")
                            //suggestions.add("$song2_song ($song2_singer)")
                            //suggestions.add("$song3_song ($song3_singer)")
                            arrayAdapter = ArrayAdapter<String>(this@MainActivity, android.R.layout.select_dialog_item, suggestions)
                            searchBar.setAdapter(arrayAdapter)
                            searchBar.refreshAutoCompleteResults()

                            var length = text.toString().length
                            //Log.i("PSG", ((end-begin).toString()))
                        }

                    }

                }
            }
        }

    }

    private fun initPython(){
        if (!Python.isStarted()){
            Python.start(AndroidPlatform(this))

        }

    }

    private fun getRequest(userInput: String): MutableList<PyObject> {
        val python = Python.getInstance()
        val pythonFile = python.getModule("request_to_do")
        return pythonFile.callAttr("main_request", userInput).asList() //return pythonFile.callAttr("main_request", userInput).toString()




    }

    private fun getRequestAutoComplete(autoCompleteInput: String): MutableList<PyObject> {
        val python = Python.getInstance()
        val pythonFile = python.getModule("request_to_do")
        return pythonFile.callAttr("auto_complete", autoCompleteInput).asList() //return pythonFile.callAttr("main_request", userInput).toString()




    }}


class Fooo (autoCompleteInput: String): Runnable {
    @Volatile
    var python = Python.getInstance()
    var pythonFile = python.getModule("request_to_do")
    var okk =  pythonFile.callAttr("auto_complete", autoCompleteInput).asList()
        private set

    override fun run() {

    }

}

