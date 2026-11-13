from utitilty import gemini_call,ollama_call,openai_call
print("-----------DASHBOARD FOR LLM CHOICE----------------")
print("\n")


choice = input("enter the LLM you want....")
question=input('enter the question\n')


match choice:
        case "1":openai_call(question)
        case "2":ollama_call(question)
        case "3":gemini_call(question)
        case _:print('NA')

