package com.aporia;

import com.aporia.commands.StructureCommand;
import org.bukkit.plugin.java.JavaPlugin;

public class Main extends JavaPlugin {

    @Override
    public void onEnable() {

        getCommand("structure")
                .setExecutor(
                        new StructureCommand()
                );

        getLogger().info(
                "Structure Plugin Enabled"
        );
    }
}