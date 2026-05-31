package com.aporia.commands;

import com.aporia.structure.BlockData;
import com.aporia.structure.StructureLoader;

import org.bukkit.Material;
import org.bukkit.World;
import org.bukkit.entity.Player;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;

import java.util.List;

public class StructureCommand implements CommandExecutor {

    @Override
    public boolean onCommand(
            CommandSender sender,
            Command command,
            String label,
            String[] args
    ) {

        if (!(sender instanceof Player player)) {

            sender.sendMessage(
                    "플레이어만 사용 가능합니다."
            );

            return true;
        }

        try {

            List<BlockData> blocks =
                    StructureLoader.load(
                            "generated_structure.json"
                    );

            World world =
                    player.getWorld();

            int baseX =
                    player.getLocation().getBlockX();

            int baseY =
                    player.getLocation().getBlockY();

            int baseZ =
                    player.getLocation().getBlockZ();

            int placed = 0;

            for (BlockData block : blocks) {

                int x =
                        baseX + block.getX();

                int y =
                        baseY + block.getY();

                int z =
                        baseZ + block.getZ();

                Material material =
                        Material.valueOf(
                                block.getBlock()
                                        .toUpperCase()
                        );

                world.getBlockAt(
                        x,
                        y,
                        z
                ).setType(material);

                placed++;
            }

            player.sendMessage(
                    "구조물 생성 완료 : "
                            + placed
                            + " blocks"
            );

        } catch (Exception e) {

            e.printStackTrace();

            sender.sendMessage(
                    "구조물 생성 실패"
            );
        }

        return true;
    }
}