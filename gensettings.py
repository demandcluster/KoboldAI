gensettingstf = [
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Output Length",
	"id": "setoutput", 
	"min": 16,
	"max": 512,
	"step": 2,
	"default": 80,
    "tooltip": "Number of tokens the AI should generate. Higher numbers will take longer to generate.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "genamt"
	},
   {
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.01,
	"default": 0.5,
    "tooltip": "Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "temp"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top P Sampling",
	"id": "settopp", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 0.9,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make text more predictable but can become repetitious. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_p"
    
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Top K Sampling",
	"id": "settopk",
	"min": 0,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "Alternative sampling method, can be combined with top_p. (Put this value on 0 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_k"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Tail Free Sampling",
	"id": "settfs", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 1.0,
    "tooltip": "Alternative sampling method; it is recommended to disable top_p and top_k (set top_p to 1 and top_k to 0) if using this. 0.95 is thought to be a good value. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "tfs"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Typical Sampling",
	"id": "settypical", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 1.0,
    "tooltip": "Alternative sampling method described in the paper \"Typical Decoding for Natural Language Generation\" (10.48550/ARXIV.2202.00666). The paper suggests 0.2 as a good value for this setting. (Put this value on 1 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "typical"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top A Sampling",
	"id": "settopa", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.01,
	"default": 0.0,
    "tooltip": "Alternative sampling method that reduces the randomness of the AI whenever the probability of one token is much higher than all the others. Higher values have a stronger effect. (Put this value on 0 to disable its effect)",
    "menu_path": "Settings",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_a"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Repetition Penalty",
	"id": "setreppen", 
	"min": 1.0,
	"max": 3.0,
	"step": 0.01,
	"default": 1.1,
    "tooltip": "Used to penalize words that were already generated or belong to the context.",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen"
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Rep Pen Range",
	"id": "setreppenrange", 
	"min": 0,
	"max": 4096,
	"step": 4,
	"default": 0,
    "tooltip": "Repetition penalty range. If set higher than 0, only applies repetition penalty to the last few tokens of your story rather than applying it to the entire story. This slider controls the amount of tokens at the end of your story to apply it to.",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen_range"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Rep Pen Slope",
	"id": "setreppenslope", 
	"min": 0.0,
	"max": 10.0,
	"step": 0.1,
	"default": 0.0,
    "tooltip": "Repetition penalty slope. If BOTH this setting and Rep Penalty Range are set higher than 0, will use sigmoid interpolation to apply repetition penalty more strongly on tokens that are closer to the end of your story. This setting controls the tension of the sigmoid curve; higher settings will result in the repetition penalty difference between the start and end of your story being more apparent. Setting this to 1 uses linear interpolation; setting this to 0 disables interpolation.",
    "menu_path": "Settings",
    "sub_path":  "Repetition",
    "classname": "model",
    "name": "rep_pen_slope"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Context Tokens",
	"id": "settknmax", 
	"min": 512,
	"max": 2048,
	"step": 8,
	"default": 1024,
    "tooltip": "Max number of tokens of context to submit to the AI for sampling. Make sure this is higher than Amount to Generate. Higher values increase VRAM/RAM usage.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "max_length"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Gens Per Action",
	"id": "setnumseq", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 1,
    "tooltip": "Number of results to generate per submission. Increases VRAM/RAM usage.",
    "menu_path": "Settings",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "numseqs"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "WI Depth",
	"id": "setwidepth", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 3,
    "tooltip": "Number of historic actions to scan for World Info keys.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "user",
    "name": "widepth"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Auto Save",
	"id": "autosave", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Whether the game is saved after each action.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "story",
    "name": "autosave"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Add Prompt",
	"id": "setuseprompt", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 1,
    "tooltip": "Whether the prompt should be sent in the context of every action.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "story",
    "name": "useprompt"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Adventure Mode",
	"id": "setadventure", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Turn this on if you are playing a Choose your Adventure model.",
    #"menu_path": "Story",
    #"sub_path": "",
    #"classname": "story",
    #"name": "adventure"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Chat Mode",
	"id": "setchatmode", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "This mode optimizes KoboldAI for chatting.",
    #"menu_path": "Story",
    #"sub_path": "",
    #"classname": "story",
    #"name": "chatmode"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Dynamic WI Scan",
	"id": "setdynamicscan", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Scan the AI's output for World Info keys as it's generating the output.",
    "menu_path": "World Info",
    "sub_path": "",
    "classname": "story",
    "name": "dynamicscan"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Prompt Gen",
	"id": "setnopromptgen", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "When enabled the AI does not generate when you enter the prompt, instead you need to do an action first.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "user",
    "name": "nopromptgen"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Prefilled Memory",
	"id": "setrngpersist",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "When enabled, the Memory text box in the Random Story dialog will be prefilled by default with your current story's memory instead of being empty.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "user",
    "name": "rngpersist"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Genmod",
	"id": "setnogenmod",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Disables userscript generation modifiers.",
    "menu_path": "Settings",
    "sub_path": "Modifiers",
    "classname": "user",
    "name": "nogenmod"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Full Determinism",
	"id": "setfulldeterminism",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Causes generation to be fully deterministic -- the model will always output the same thing as long as your story, settings and RNG seed are the same. If this is off, only the sequence of outputs that the model makes will be deterministic."
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Debug",
	"id": "debug",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Show debug info",
    "menu_path": "",
    "sub_path": "",
    "classname": "user",
    "name": "debug"
	},
    {
    "uitype": "dropdown",
	"unit": "text",
	"label": "Story Mode",
	"id": "storymode",
	"default": 0,
    "tooltip": "Choose the mode of KoboldAI.",
    "menu_path": "Home",
    "sub_path": "",
    "classname": "story",
    "name": "storymode",
    'children': [{'text': 'Story', 'value': 0}, {'text':'Adventure','value':1}, {'text':'Chat', 'value':2}]
    },
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Streaming",
 	"id": "setoutputstreaming",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Shows outputs to you as they are made.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "output_streaming"
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Probabilities",
 	"id": "setshowprobs",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds context menu to outputs showing what other words were considered as it was built.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "show_probs"
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Text Gen",
 	"id": "alttextgen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Inserts world info entries behind text that first triggers them for better context with unlimited depth.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "alt_gen"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Trim Sentences",
 	"id": "frmttriminc",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Remove text after last sentence closure.  If no closure is found, all tokens will be returned.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmttriminc"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Blank Lines",
 	"id": "frmtrmblln",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Replace double newlines (\\n\\n) with single newlines to avoid blank lines.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmblln"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Special Chars",
 	"id": "frmtrmspch",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Remove special characters (@,#,%,^, etc).",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmspch"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Auto Spacing",
 	"id": "frmtadsnsp",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Add spaces automatically if needed.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtadsnsp"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Single Line",
 	"id": "singleline",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Only allows the AI to output anything before the enter",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "singleline"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "slider",
 	"unit": "int",
 	"label": "AN Depth",
 	"id": "singleline",
 	"min": 1,
 	"max": 5,
 	"step": 1,
 	"default": 3,
	"tooltip": "The Author's Note will be entered this many actions back from the end of the game text",
    "menu_path": "author_notes",
    "sub_path": "",
    "classname": "story",
    "name": "andepth"
 	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Show Field Budget",
	"id": "setshowbudget",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Shows token usage when typing in relevant text boxes. <b>May lag slower devices.</b>"
	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Beep on Complete",
 	"id": "beep_on_complete",
 	"min": 1,
 	"max": 5,
 	"step": 1,
 	"default": 3,
	"tooltip": "When enabled the UI will beep when completing an action such as generation or model loading.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "beep_on_complete"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "dropdown",
	"unit": "text",
	"label": "Image Priority",
	"id": "img_gen_priority",
	"default": 1,
    "tooltip": "Determine where images will be generated.",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "user",
    "name": "img_gen_priority",
    'children': [{'text': 'Use Local Only', 'value': 0}, {'text':'Prefer Local','value':1}, {'text':'Prefer Horde', 'value':2}, {'text':'Use Horde Only', 'value':3}]
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Model in memory",
 	"id": "keep_img_gen_in_memory",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "If enabled, the system will keep the model in memory speeding up image generation times",
    "menu_path": "Interface",
    "sub_path": "Images",
    "classname": "system",
    "name": "keep_img_gen_in_memory"
 	},
]

gensettingsik =[{
	"uitype": "slider",
	"unit": "float",
	"label": "Temperature",
	"id": "settemp", 
	"min": 0.1,
	"max": 2.0,
	"step": 0.05,
	"default": 0.5,
    "tooltip": "Randomness of sampling. High values can increase creativity but may make text less sensible. Lower values will make text more predictable but can become repetitious.",
    "menu_path": "Model",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "temp"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Top P Sampling",
	"id": "settopp", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.05,
	"default": 1.1,
    "tooltip": "Used to discard unlikely text in the sampling process. Lower values will make text more predictable but can become repetitious.",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_p"
	},
	{
	"uitype": "slider",
	"unit": "int",
	"label": "Top K Sampling",
	"id": "settopk",
	"min": 0,
	"max": 100,
	"step": 1,
	"default": 0,
    "tooltip": "Alternative sampling method, can be combined with top_p.",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "top_k"
	},
	{
	"uitype": "slider",
	"unit": "float",
	"label": "Tail Free Sampling",
	"id": "settfs", 
	"min": 0.0,
	"max": 1.0,
	"step": 0.05,
	"default": 0.0,
    "tooltip": "Alternative sampling method; it is recommended to disable (set to 0) top_p and top_k if using this. 0.95 is thought to be a good value.",
    "menu_path": "Model",
    "sub_path":  "Sampling",
    "classname": "model",
    "name": "tfs"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "Output Length",
	"id": "setikgen", 
	"min": 50,
	"max": 3000,
	"step": 2,
	"default": 200,
    "tooltip": "Number of characters the AI should generate.",
    "menu_path": "Model",
    "sub_path":  "Generation",
    "classname": "model",
    "name": "max_length"
	},
    {
	"uitype": "slider",
	"unit": "int",
	"label": "WI Depth",
	"id": "setwidepth", 
	"min": 1,
	"max": 5,
	"step": 1,
	"default": 3,
    "tooltip": "Number of historic actions to scan for World Info keys.",
    "menu_path": "User",
    "classname": "user",
    "name": "widepth"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Auto Save",
	"id": "autosave", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Whether the game is saved after each action.",
    "menu_path": "Story",
    "classname": "story",
    "name": "autosave"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Add Prompt",
	"id": "setuseprompt", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 1,
    "tooltip": "Whether the prompt should be sent in the context of every action.",
    "menu_path": "Story",
    "classname": "story",
    "name": "useprompt"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Adventure Mode",
	"id": "setadventure", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "Turn this on if you are playing a Choose your Adventure model.",
    #"menu_path": "Story",
    #"classname": "story",
    #"name": "adventure"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Chat Mode",
	"id": "setchatmode", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "This mode optimizes KoboldAI for chatting.",
    #"menu_path": "Story",
    #"classname": "story",
    #"name": "chatmode"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "No Prompt Gen",
	"id": "setnopromptgen", 
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "When enabled the AI does not generate when you enter the prompt, instead you need to do an action first.",
    "menu_path": "User",
    "classname": "user",
    "name": "nopromptgen"
	},
	{
	"uitype": "toggle",
	"unit": "bool",
	"label": "Prefilled Memory",
	"id": "setrngpersist",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
    "tooltip": "When enabled, the Memory text box in the Random Story dialog will be prefilled by default with your current story's memory instead of being empty.",
    "menu_path": "User",
    "classname": "user",
    "name": "rngpersist"
	},
    {
	"uitype": "toggle",
	"unit": "bool",
	"label": "Debug",
	"id": "debug",
	"min": 0,
	"max": 1,
	"step": 1,
	"default": 0,
  "tooltip": "Show debug info",
    "menu_path": "User",
    "classname": "user",
    "name": "debug"
	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Streaming",
 	"id": "setoutputstreaming",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Shows outputs to you as they are made.",
    "menu_path": "User",
    "classname": "user",
    "name": "output_streaming"
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Token Probabilities",
 	"id": "setshowprobs",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Adds context menu to outputs showing what other words were considered as it was built.",
    "menu_path": "Interface",
    "sub_path": "UI",
    "classname": "user",
    "name": "show_probs"
 	},
    {
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Alt Text Gen",
 	"id": "alttextgen",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Inserts world info entries behind text that first triggers them for better context with unlimited depth.",
    "menu_path": "Settings",
    "sub_path": "Other",
    "classname": "system",
    "name": "alt_gen"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Trim Sentences",
 	"id": "frmttriminc",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Remove text after last sentence closure.  If no closure is found, all tokens will be returned.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmttriminc"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Blank Lines",
 	"id": "frmtrmblln",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Replace double newlines (\\n\\n) with single newlines to avoid blank lines.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmblln"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "No Special Chars",
 	"id": "frmtrmspch",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Remove special characters (@,#,%,^, etc).",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtrmspch"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Auto Spacing",
 	"id": "frmtadsnsp",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Add spaces automatically if needed.",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "frmtadsnsp"
 	},
    {
    "UI_V2_Only": True,
 	"uitype": "toggle",
 	"unit": "bool",
 	"label": "Single Line",
 	"id": "singleline",
 	"min": 0,
 	"max": 1,
 	"step": 1,
 	"default": 0,
	"tooltip": "Only allows the AI to output anything before the enter",
    "menu_path": "Interface",
    "sub_path": "Formatting",
    "classname": "user",
    "name": "singleline"
 	},
]

formatcontrols = [{
    "label": "Trim incomplete sentences",
    "id": "frmttriminc",
    "tooltip": "Remove text after last sentence closure.  If no closure is found, all tokens will be returned."
    },
    {
    "label": "Remove blank lines",
    "id": "frmtrmblln",
    "tooltip": "Replace double newlines (\\n\\n) with single newlines to avoid blank lines."
    },
    {
    "label": "Remove special characters",
    "id": "frmtrmspch",
    "tooltip": "Remove special characters (@,#,%,^, etc)."
    },
    {
    "label": "Automatic spacing",
    "id": "frmtadsnsp",
    "tooltip": "Add spaces automatically if needed."
    },
    {
    "label": "Single Line",
    "id": "singleline",
    "tooltip": "Only allows the AI to output anything before the enter"
    }]
