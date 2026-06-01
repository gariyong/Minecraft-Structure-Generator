package com.aporia.commands;

import com.aporia.structure.BlockData;
import com.aporia.structure.JsonStructureLoader;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

import java.io.File;
import java.util.List;

public class GenerateCastleCommand
        implements CommandExecutor {

    @Override
    public boolean onCommand(
            CommandSender sender,
            Command command,
            String label,
            String[] args
    ) {

        if (!(sender instanceof Player player)) {
            return true;
        }

        try {

            File file = new File(
                    "generated_castle.json"
            );

            List<BlockData> blocks =
                    JsonStructureLoader.load(file);

            JsonStructureLoader.generateStructure(
                    player.getLocation(),
                    blocks
            );

            player.sendMessage(
                    "§aCastle Generated!"
            );

        } catch (Exception e) {

            e.printStackTrace();

            player.sendMessage(
                    "§cFailed to load structure."
            );
        }

        return true;
    }
}