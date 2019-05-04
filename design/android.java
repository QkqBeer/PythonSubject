<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">
    <RelativeLayout
        android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:id="@+id/login_layout"
        android:layout_marginLeft="20dp"
        android:layout_marginRight="20dp"
        android:gravity="center">
		//将账号文本框放好
        <FrameLayout
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:id="@+id/usename_layout"
            android:layout_marginTop="55dp"
            android:gravity="center">

            <EditText
                android:layout_width="fill_parent"
                android:layout_height="40dp"
                android:id="@+id/usename"
                android:layout_marginTop="5dp"
                android:inputType="number"
                android:paddingRight="60dp"
                android:maxLength="20"
                android:paddingLeft="55dp"
                android:paddingTop="5dp"/>

            <TextView
                android:layout_width="50dp"
                android:layout_height="35dp"
                android:layout_marginStart="8dp"
                android:layout_gravity="left|center_vertical"
                android:text="@string/longin"
                android:textSize="20dp"
                android:layout_marginLeft="8dp" />

        </FrameLayout>
        ////将密码文本框放好
        <FrameLayout
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:id="@+id/usecode_layout"
            android:layout_below="@id/usename_layout"
            android:layout_marginTop="6dp"
            android:gravity="center" >

            <EditText
                android:id="@+id/password"
                android:layout_width="fill_parent"
                android:layout_height="55dp"
                android:inputType="textPassword"
                android:maxLength="20"
                android:paddingLeft="55dp"
                android:paddingRight="60dp"
                android:paddingTop="5dp"/>

            <TextView
                android:layout_width="50dp"
                android:layout_height="35dp"
                android:layout_marginStart="8dp"
                android:layout_gravity="left|center_vertical"
                android:text="@string/longin"
                android:textSize="20dp"
                android:layout_marginLeft="8dp" />

        </FrameLayout>
		//三个按钮
        <Button
            android:id="@+id/login"//登录按钮
            android:layout_width="fill_parent"
            android:layout_height="44dp"
            android:layout_below="@id/usecode_layout"
            android:layout_marginTop="30dp"
            android:background="#ff336699"
            android:textColor="@android:color/white"
            android:gravity="center"
            android:text="登录" />
        <Button
            android:id="@+id/login_error"//忘记密码的按钮
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignRight="@id/login"
            android:layout_below="@id/login"
            android:background="#00000000"
            android:text="忘记密码"
            android:textSize="16sp" />
        <Button
            android:id="@+id/register"//注册按钮
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_alignLeft="@id/login"
            android:layout_below="@id/login"
            android:background="#00000000"
            android:gravity="left|center_vertical"
            android:text="注册"
            android:textSize="16sp"
            android:visibility="visible" />

    </RelativeLayout>
</LinearLayout>