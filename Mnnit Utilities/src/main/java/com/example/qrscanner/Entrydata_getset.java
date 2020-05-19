package com.example.qrscanner;

public class Entrydata_getset {
    private String id,name,room_no,reg_no,out,in,image_url;
  /*  public Entrydata_getset(String id,String name,String room_no,String reg_no,String out,String in,String image_url){}
    {
        this.id=id;
        this.name=name;
        this.room_no=room_no;
        this.reg_no=reg_no;
        this.out=out;
        this.in=in;

    }*/

    public Entrydata_getset(String id, String name, String regno, String roomno, String intime, String outtime) {
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRoom_no() {
        return room_no;
    }

    public void setRoom_no(String room_no) {
        this.room_no = room_no;
    }

    public String getReg_no() {
        return reg_no;
    }

    public void setReg_no(String reg_no) {
        this.reg_no = reg_no;
    }

    public String getOut() {
        return out;
    }

    public void setOut(String out) {
        this.out = out;
    }

    public String getIn() {
        return in;
    }

    public void setIn(String in) {
        this.in = in;
    }
}
