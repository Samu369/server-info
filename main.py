def srv_info(token: str, serverid: int):
    import tkinter as tk
    import discord, datetime
    try:
        intents = discord.Intents.default()
        intents.all()
        client = discord.Client(intents=intents)
        @client.event
        async def on_ready():
            global all_info
            now = datetime.datetime.now()
            server = client.get_guild(serverid)
            if server:
                server_info = f"--- INFORMAZIONI GENERALI ---\nServer Name: {server.name}\nServer ID: {server.id}\nOwner: {server.owner}\nMember Count: {server.member_count}\nVerification Level: {server.verification_level}\nCreation Time: {server.created_at}\n"
                server_info += f"AFK Timeout: {server.afk_timeout} seconds\nAFK Channel: {server.afk_channel}\nExplicit Content Filter: {server.explicit_content_filter}\n"
                server_info += f"Default Notifications: {server.default_notifications}\nMFA Level: {server.mfa_level}\nBoost Tier: {server.premium_tier}\nBoost Count: {server.premium_subscription_count}\n"
                server_info += f"Server Features: {', '.join(server.features)}\nSplash Image URL: {server.splash}\nBanner Image URL: {server.banner}\n"
                server_info += f"Emojis: {', '.join([str(emoji) for emoji in server.emojis])}\nMax File Size: {server.filesize_limit} bytes\nMax Members: {server.max_members}\n"
                server_info += f"System Channel: {server.system_channel}\nRules Channel: {server.rules_channel}\nPublic Updates Channel: {server.public_updates_channel}\n"
                
                roles_info = "\n--- INFORMAZIONI RUOLI ---\n"
                for role in server.roles:
                    roles_info += f"Role Name: {role.name}\nRole ID: {role.id}\nColor: {role.color}\nPermissions: {role.permissions}\nPosition: {role.position}\nMentionable: {role.mentionable}\nHoisted: {role.hoist}\n\n"
                
                channels_info = "\n--- INFORMAZIONI CANALI ---\n"
                for channel in server.channels:
                    channels_info += f"Channel Name: {channel.name}\nChannel ID: {channel.id}\nType: {channel.type}\nPosition: {channel.position}\nCategory: {channel.category}\n"
                    if isinstance(channel, discord.TextChannel):
                        channels_info += f"Permissions Synced: {channel.permissions_synced}\nSlowmode Delay: {channel.slowmode_delay} seconds\nNSFW: {channel.is_nsfw()}\nTopic: {channel.topic}\n"
                        everyone_permissions = channel.overwrites_for(server.default_role)
                        permissions_text = "\n".join([f"{permission}: {allowed}" for permission, allowed in everyone_permissions])
                        channels_info += f"Default Role Permissions:\n{permissions_text}\n"
                    elif isinstance(channel, discord.VoiceChannel):
                        channels_info += f"Bitrate: {channel.bitrate} bps\nUser Limit: {channel.user_limit}\n"
                    channels_info += "\n"
                
                members_info = "\n--- INFORMAZIONI MEMBRI ---\n"
                for member in server.members:
                    members_info += f"Member Name: {member.name}\nMember ID: {member.id}\nNick: {member.nick}\nStatus: {member.status}\nActivity: {member.activity}\nJoined At: {member.joined_at}\nRoles: {', '.join([role.name for role in member.roles])}\n\n"
                
                all_info = f"--- SERVER INFO (by Samu369) ---\nGitHub: []\nData e Ora: {now.day}/{now.month}/{now.year} {now.hour}:{now.minute}\n\n" + server_info + roles_info + channels_info + members_info
            else:
                print("\nErrore: Il server non esiste o il bot non è nel server!")
            await client.close()
        client.run(token)
        print("Informazioni del server mostrate in una nuova finestra")
        i = tk.Tk()
        i.geometry("960x540")
        i.title("Server info (by Samu369)")
        i.configure(background="black")
        txt = tk.Text(i, background="black", wrap=tk.WORD, fg="white", font=("Arial", 10))
        txt.insert(tk.END, all_info)
        txt.config(state=tk.DISABLED)
        txt.pack(fill=tk.BOTH, expand=True)
        i.mainloop()
    except Exception as e:
        print(f"Errore: {e}\n")


if __name__ == "__main__":
    print("""  _____                            _____        __      
 / ____|                          |_   _|      / _|     
| (___   ___ _ ____   _____ _ __    | |  _ __ | |_ ___  
 \___ \ / _ \ '__\ \ / / _ \ '__|   | | | '_ \|  _/ _ \ 
 ____) |  __/ |   \ V /  __/ |     _| |_| | | | || (_) |
|_____/ \___|_|    \_/ \___|_|    |_____|_| |_|_| \___/ 
                                        by Samu369\n""")
    tok = input("Inserisci il token del bot: ")
    ids = input("Inserisci l'id del server: ")

    print("\nRaccolta informazioni sul server in corso...")
    srv_info(tok, int(ids))