package com.aporia.structure;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.World;

import java.io.File;
import java.io.FileReader;
import java.lang.reflect.Type;
import java.util.List;

public class JsonStructureLoader {

    public static List<BlockData> load(File file)
            throws Exception {

        Gson gson = new Gson();

        Type type =
                new TypeToken<List<BlockData>>() {}.getType();

        return gson.fromJson(
                new FileReader(file),
                type
        );
    }

    public static void generateStructure(Location origin, List<BlockData> blocks) {
        World world = origin.getWorld();
        for (BlockData data : blocks) {

                int x = origin.getBlockX() + data.getX();
                int y = origin.getBlockY() + data.getY();
                int z = origin.getBlockZ() + data.getZ();

                Material material =
                        Material.matchMaterial(
                                data.getBlock().toUpperCase()
                        );

                if (material == null)
                continue;

                world.getBlockAt(
                        x,
                        y,
                        z
                ).setType(material);
        }
    }
}