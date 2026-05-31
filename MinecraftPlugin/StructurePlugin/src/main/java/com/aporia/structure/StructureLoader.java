package com.aporia.structure;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.lang.reflect.Type;
import java.util.List;

public class StructureLoader {

    public static List<BlockData> load(
            String path
    ) throws Exception {

        Gson gson = new Gson();

        Type type =
                new TypeToken<List<BlockData>>() {
                }.getType();

        return gson.fromJson(
                new FileReader(path),
                type
        );
    }
}