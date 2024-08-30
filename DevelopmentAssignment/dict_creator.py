#function to format the outputs
def create_dict(outputs, timesents=None, timerecvds=None,for_server=False, ClientID =None, iterative=True):
    l = []
    if iterative:
        for output in outputs:
            d = {}
            msg = output[0]["generated_text"].split("\n\n")
            d["Prompt"] = msg[0]
            d["Message"] = msg[1:]
            d["Source"] = "gpt-2"
            if(for_server):
                d["ClientID"] = ClientID
            l.append(d)
    else:
        d = {}
        msg = outputs[0]["generated_text"].split("?")
        d["Prompt"] = msg[0]
        d["Message"] = msg[1:]
        d["Source"] = "gpt-2"
        if(for_server):
            d["ClientID"] = ClientID
        l.append(d)

    
    return l