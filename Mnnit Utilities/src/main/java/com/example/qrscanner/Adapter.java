package com.example.qrscanner;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {

    LayoutInflater layoutInflater;
    List<Entrydata_getset>entrydata_list;

    public Adapter(List<Entrydata_getset> entrydata_list)
    {
        this.entrydata_list=entrydata_list;

    }


    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater layoutInflater=LayoutInflater.from(parent.getContext());
       View view=layoutInflater.inflate(R.layout.student_list,parent,false);
        return new ViewHolder(view);

    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {

        holder.id.setText(entrydata_list.get(position).getId());
        holder.name.setText(entrydata_list.get(position).getName());
        holder.room_no.setText(entrydata_list.get(position).getRoom_no());
        holder.reg_no.setText(entrydata_list.get(position).getReg_no());
        holder.out.setText(entrydata_list.get(position).getOut());
        holder.in.setText(entrydata_list.get(position).getIn());

    }

    @Override
    public int getItemCount() {
        return entrydata_list.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {
        TextView id,name,room_no,reg_no,out,in;

        public ViewHolder(@NonNull View itemview)
        {
            super(itemview);


            id=itemview.findViewById(R.id.tv_id);
            name=itemview.findViewById(R.id.tv_student_name);
            room_no=itemview.findViewById(R.id.tv_room);
            reg_no=itemview.findViewById(R.id.tv_reg);
            out=itemview.findViewById(R.id.tv_out);
            in=itemview.findViewById(R.id.tv_in);




        }
    }
}
