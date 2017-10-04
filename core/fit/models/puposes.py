
public class Purpose:IEntity
    {
        public int Id { get; set; }
        public string PurposeString { get; set; }
        public string PurposeQuestion { get; set; }
        public bool IsActive { get; set; }
    }

public class PurposeAnswer: IEntity
    {
        public int Id { get; set; }
        public int PurposeId { get; set; }
        public int DreamBuilderId { get; set; }
        public string PurposeAnswerString { get; set; }
    }

public class PurposeList:IEntity 
    {
        public int Id { get; set; }
        public string Question { get; set; }
        public string Answer { get; set; }
        public bool IsChecked { get; set; }
        public int PurposeId { get; set; }
        public int AnswerId { get; set; }
        public string Placeholder { get; set; }
    }


public class PurposeStatement:IEntity
    {
        public int Id { get; set; }
        public int DreamBuilderId { get; set; }
        public string PurposeStatementString { get; set; }
    }
